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
prompt = "Suggest a name for my cloth company"

message_system = {
    "role": "system",
    "content": "You are a brand manager who suggest name for my cloth company. Name should be in one word, suggest only one name"
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]
response = client.chat.completions.create (model = model, messages = messages, temperature = 2)


print("#" * 20)
answer = response.choices[0].message.content
print(answer)