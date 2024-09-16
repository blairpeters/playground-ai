import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [{"role": "user", "content": "What is the capital of New York?"}]
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )

    print(response.choices[0].message["content"])
except Exception as e:
    print(e)