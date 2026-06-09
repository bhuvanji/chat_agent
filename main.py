import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

async def chat_agent():
    while True:
        user_input = input("Bhuvan: ")
        if user_input.lower() == "exit":
            print("ChatAgent goodbye!")
            break
        
        #Send user input to OpenAIand get response
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "You are a smart helpful assistant who answer user query very intelligently."},
                {"role": "user", "content": user_input}
            ]
        )
        # Extract and print response
        print("Agent:", response.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(chat_agent())
    