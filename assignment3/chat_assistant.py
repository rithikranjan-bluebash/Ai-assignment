import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

print("🤖 Conversational AI Assistant")
print("Type 'exit' to quit\n")

# Chat history storage
chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Add user message to history
    chat_history.append(HumanMessage(content=user_input))

    # Send entire conversation history
    response = llm.invoke(chat_history)

    # Store assistant response
    chat_history.append(AIMessage(content=response.content))

    print("\nAssistant:", response.content)
    print("\n--------------------------\n")