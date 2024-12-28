from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os   
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":

    # Define the prompt template
    summary_prompt = """
    You are a translator where you will be given input text
    {input}
    you need to translate that input text into the desired language i.e {convertLanguage}    
    """

    # Create a PromptTemplate instance
    prompt_template = PromptTemplate(input_variables=["input", "convertLanguage"], template=summary_prompt)

    # Initialize the ChatGoogleGenerativeAI model with your API key
    llm = ChatGoogleGenerativeAI(
        model='gemini-1.5-flash',
        api_key=os.getenv('GOOGLE_API_KEY')
    )

    # Create a chain with prompt, model, and output parser
    chain = prompt_template | llm | StrOutputParser()

    # Ask the user for the input text and the language to translate into
    input_text = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g., Spanish, French, etc.): ")

    # Call the chain with user inputs
    res = chain.invoke({"input": input_text, "convertLanguage": target_language})

    # Print the translated text
    print(f"Translated text: {res}")
