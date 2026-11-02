import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROK_API_KEY")
if not my_api_key:
    raise ValueError("GROK API KEY NOT FOUND")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "Do you know Virat Kohli?"
message = {
    "role": role,
    "content": prompt
}

messages = [message]
response = client.chat.completions.create (model = model, messages = messages)

print(response)
print("#" * 20)
answer = response.choices[0].message.content
print(answer)