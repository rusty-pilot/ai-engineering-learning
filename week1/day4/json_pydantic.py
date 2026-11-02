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

from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information strictly based on the following schema and give a json output: {schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}
text = "Hello my name is Ratnesh. I have an iphone which is not working at all. My address is delhi. My email is ratneshpuri52@gmail.com. My contact number is 9914172214."
prompt = f"""
This is a customer ticket. Please extract the personal information from {text}
"""

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]
response = client.chat.completions.create (model = model, messages = messages, temperature=2, response_format=response_format)


answer = response.choices[0].message.content
print(answer)


# Parsing the JSON response into a Pydantic model
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket= Ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)
