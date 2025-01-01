from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool
from langchain.tools.render import render_text_description
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv("GOOGLE_API_KEY")

@tool
def reverse_string(input_string: str) -> str:
    """
    Reverses the given string.
    """
    print(f"Reversing string: {input_string}")
    return input_string[::-1]

@tool
def count_words_in_string(input_string: str) -> int:
    """
    Counts the number of words in the string.
    """
    print(f"Counting words in string: {input_string}")
    return len(input_string.split())

if __name__ == "__main__":
    # Initialize the LLM with the API key
    llm = ChatGoogleGenerativeAI(
        api_key=API_KEY,
        temperature=1,
        model="gemini-1.5-flash",
        max_tokens=1024,
    )

    # List of tools (replacing the previous one)
    tools = [reverse_string, count_words_in_string]

    # Define the prompt template
    template = """
    Answer the following questions as best as you can.
    You have access to the following tools:
    {tools}
     Use the following format:
     
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action (just the value, no function call syntax)
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the input question
    
    Begin!
    Question: {input}
    Thought:
    """

    # Prepare the prompt
    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([tool.name for tool in tools])
    )

    # Create a chain that links the prompt and the LLM
    chain = prompt | llm

    # Define input questions
    input_questions = [
        "What is the reverse of 'Hello World'?",
        "How many words are in 'This is a test sentence'?"
    ]

    # Run the chain for each input question
    for question in input_questions:
        res = chain.invoke({"input": question})
        print(f"Question: {question}")
        print(res)
