from langchain.chains.conversation.memory import ConversationBufferWindowMemory
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


# It creates a window memory for the conversation that keeps track of last k interactions
memory = ConversationBufferWindowMemory(k=2)  # Example here it will last for 2 interactions in memory

# Initialize the chat model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                 api_key=API_KEY )
# It creates a conversation chain with the chat model and the window memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
)

while True:
    # Here we are taking user input
    user_input = input("\nYou: ")
    
    # Check for exit command
    if user_input.lower() in ['bye', 'exit']:
        print("Goodbye!")

        # Print the conversation history within the window
        print(conversation.memory.buffer)
        break
    
    # Here we are getting the response from the AI
    response = conversation.predict(input=user_input)
    print("\nAI:", response)