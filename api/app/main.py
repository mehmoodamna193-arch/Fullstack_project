import os 
import sys
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv() # .env file 

llm = init_chat_model(
    model=os.getenv("MODEL_NAME"),
    temperature=1.0
)

# System Message
history = [{
    "role": "system",
    "content": "You are a helpful Cue AI assistant!"
}]

print("Welcome to Cue chat!")
while True:
    question = input("You: ")

    if not question:
        continue

    if question in ("exit", "quit", "bye", "q"):
        break

    # Human Message 
    history.append({
        "role": "user",
        "content": question
    })
    response = llm.invoke(history)
    history.append({
        "role": "assistant",
        "content": response.content
    }) # AI Message 

    print(f"Bot: {response.content}")

print("Goodbye!")