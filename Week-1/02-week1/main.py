from openai import OpenAI

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))
# print(os.getenv("OPENAI_MODEL"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = []
user_input = ""
system_response = ""

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    user_dic = {
        "role": "user",
        "content": user_input,
    }

    messages.append(user_dic)

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL"),
        input=messages,
    )
    ai_response = response.output_text
    system_dic = {
        "role": "assistant",
        "content": ai_response,
    }

    messages.append(system_dic)

    print("\n========== Conversation History ==========")

    for message in messages:
        print(f"{message['role'].title()} : {message['content']}")

    print("==========================================")

# print(response.output_text)

# llm = ChatOpenAI(model_name="gpt-5.3-codex", api_key=os.getenv("OPENAI_API_KEY"))
# response =llm.invoke("Hello, who is the PM of pakistan?")
# print(response.content)

# chat_anthropic = ChatAnthropic(model_name="claude-sonnet-4-6", api_key=os.getenv("ANTHROPIC_API_KEY"))
# response_anthropic = chat_anthropic.invoke("Hello, who is the PM of pakistan?")
# print(response_anthropic.content)
