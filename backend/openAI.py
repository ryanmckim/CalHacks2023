from dotenv import load_dotenv
import openai

def openai_prompt(prompt):
    conversation = [
        {"role": "user", "content": "Give me the mood, genre, feeling of this description: \"" + prompt + "\""}
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