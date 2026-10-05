from openai import OpenAI

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
load_dotenv()

#print(os.getenv("OPENAI_API_KEY"))
#print(os.getenv("OPENAI_MODEL"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.responses.create(
    model=os.getenv("OPENAI_MODEL"),
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Hello, who is the PM of Pakistan?"
                }
            ]
        }
    ]
    
)
print(response.output_text)

#llm = ChatOpenAI(model_name="gpt-5.3-codex", api_key=os.getenv("OPENAI_API_KEY"))
#response =llm.invoke("Hello, who is the PM of pakistan?")
#print(response.content)

#chat_anthropic = ChatAnthropic(model_name="claude-sonnet-4-6", api_key=os.getenv("ANTHROPIC_API_KEY"))
#response_anthropic = chat_anthropic.invoke("Hello, who is the PM of pakistan?")
#print(response_anthropic.content)