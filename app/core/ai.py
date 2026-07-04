import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_ai(messages: list):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=False
    )

    return response.choices[0].message.content
