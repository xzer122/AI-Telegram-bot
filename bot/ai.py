import os

from openai import OpenAI

from bot import texts

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_message(context=None):
    if context is None:
        context = [
            {"role": "system", "content": texts.prompt},
            {"role": "user", "content": "/start"}
        ]
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=context,
        max_tokens=7000
    )
    return completion
