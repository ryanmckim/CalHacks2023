import cv2
import os
import numpy as np
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, AutoProcessor, MusicgenForConditionalGeneration

import scipy # for saving to wav file
import openai
from dotenv import load_dotenv # for loading api keys


class BlipModelSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls._create_instance()
        return cls._instance

    @classmethod
    def _create_instance(cls):
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
        return processor, model

class MusicModelSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls._create_instance()
        return cls._instance

    @classmethod
    def _create_instance(cls):
        music_processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
        music_model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
        return music_processor, music_model


def create_snapshots(video_path, output_path='output_frames', interval_seconds=2):
    cap = cv2.VideoCapture(video_path)
    directory = output_path
    os.makedirs(directory, exist_ok=True)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval_seconds = interval_seconds
    interval_frames = int(fps * interval_seconds)
    count = 1
    
    if not cap.isOpened():
        print("Error opening video file")
    else:
        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()
    
            if not ret:
                break
    
            if count % interval_frames == 0:
                output_path = os.path.join(directory, f"frame_{count}.jpg")
                cv2.imwrite(output_path, frame)
                print(f"Saved frame {count}")
            count += 1
        cap.release()


# output directory is a directory of jpg images, returns a list of string captions
def caption_snapshots(directory):
    processor, model = BlipModelSingleton.get_instance()
    snapshots = []
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                raw_image = cv2.imread(os.path.join(directory, filename))
                raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
                # unconditional image captioning
                inputs = processor(raw_image, return_tensors="pt")
                out = model.generate(**inputs)
                snapshots.append(processor.decode(out[0], skip_special_tokens=True))
    else:
        print(f"Directory '{directory}' does not exist.")
    return snapshots


def openai_prompt(prompt):
    conversation = [
        {"role": "user", "content": "Give me the mood, genre, and feeling of this description: \"" + prompt + "\""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    conversation.append({"role": "user", "content": "Summarize your response in the format of the example: \"80s pop track with bassy drums and synth.\""})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    return response['choices'][0]['message']['content']


# Function for generating audio from text descriptions
def generate_audio(descriptions, path="musicgen_out.wav"):
    processor, model = MusicModelSingleton.get_instance()
    #descriptions = ["acoustic folk song to play during roadtrips: guitar flute choirs"]
    inputs = processor(
        text=descriptions,
        padding=True,
        return_tensors="pt",
    )
    audio_values = model.generate(**inputs, do_sample=True, guidance_scale=3, max_new_tokens=512)
    sampling_rate = model.config.audio_encoder.sampling_rate
    scipy.io.wavfile.write(path, rate=sampling_rate, data=audio_values[0, 0].numpy())


def main():
    try:
        np.random.seed(45)
        load_dotenv()
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        output_path = 'data/output_frames'
        create_snapshots('data/nature.mp4', output_path)
        captions = caption_snapshots(output_path)
        music_description = openai_prompt(captions)
        generate_audio(music_description, path="musicgen_out.wav")

    except Exception as e:
        print(f"An error occurred: {e}")
    

if __name__ == "__main__":
    main()