from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

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