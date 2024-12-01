import os

from openai import OpenAI

from bot import texts

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_message(text='', context=None):
    if context is None:
        context = []
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": texts.prompt},
            {"role": "user", "content": "/start"}
        ]
    )
    return completion


print(generate_message())
