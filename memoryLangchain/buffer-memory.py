from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure the API key is loaded
if not API_KEY:
    raise ValueError("API key not found. Ensure you have a .env file with GOOGLE_API_KEY set.")

# Create a memory for the conversation
memory = ConversationBufferMemory()

# Initialize the chat model with the API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=API_KEY  # Pass the API key
)

# Create a conversation chain with the chat model and the memory
conversation = ConversationChain(
    llm=llm, 
    memory=memory,
)

while True:
    # Take user input
    user_input = input("\nYou: ")
    
    # Check for exit command
    if user_input.lower() in ['bye', 'exit']:
        print("Goodbye!")

        # Print the conversation history
        print("\nConversation History:")
        print(conversation.memory.buffer)
        break
    
    # Get the response from the AI
    response = conversation.predict(input=user_input)
    print("\nAI:", response)
