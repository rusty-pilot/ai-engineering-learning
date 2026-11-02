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
prompt1 = "Hi"
prompt2 = "Explain time travel in detail"
prompt3 = "Write a 1000 words essay on Machine Learning"

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]
    response = client.chat.completions.create (model = model, messages = messages ,max_tokens=5000)
    usage = response.usage
    print(f"Prompt: {prompt}")
    print(f"Usage: {usage.prompt_tokens} prompt tokens, {usage.completion_tokens} completion tokens, {usage.total_tokens} total tokens, Finish reason: {response.choices[0].finish_reason}")
    print("#" * 20)
    answer = response.choices[0].message.content
    # print(answer)