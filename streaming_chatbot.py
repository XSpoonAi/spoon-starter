"""
Simple streaming ChatBot demo .
"""
import asyncio
from typing import Optional

from dotenv import load_dotenv

from spoon_ai.chat import ChatBot

load_dotenv()

Questions = [
    "Give me a concise overview of the Neo blockchain.",
    "List three real-world use cases for agentic OSes like SpoonOS.",
    "Draft a short tweet announcing the Spoon starter demo.",
]

def create_chatbot() -> ChatBot:
    return ChatBot()

async def stream_chatbot_response(question: str, timeout: float = 60.0) -> None:
    chatbot = create_chatbot()
    messages = [{"role": "user", "content": question}]

    async for chunk in chatbot.astream(messages, timeout=timeout):
        print(chunk.delta, end="", flush=True)

async def main():
    print(" Streaming ChatBot Demo")
    print("=" * 50)

    for question in Questions:
        print("\n" + "=" * 50)
        print(f"Q: {question}")
        print("=" * 50)
        await stream_chatbot_response(question)

if __name__ == "__main__":
    asyncio.run(main())

