from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain

# Initialize conversation memory
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Initialize the LLM using ChatGoogleGenerativeAI

# Create the conversation chain
memory = ConversationSummaryMemory(llm=llm, 
            return_message=True,
            max_token_limit=200,
    )

conversation= ConversationChain(
    llm=llm,
    memory=memory,
)

# Start conversation loop
while True:
    user_input = input("\nYou: ")

    # Exit condition
    if user_input.lower() in ['bye', 'exit']:
        print("Goodbye!")
        # Print memory buffer before exiting
        print(conversation.memory.buffer)
        break

    # Get AI response
    response = conversation.predict(input=user_input)
    print("\nAI:", response)
