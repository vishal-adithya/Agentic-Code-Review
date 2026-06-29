from langchain.agents import create_agent
from langchain.tools import tool
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound
from langchain_core.output_parsers import StrOutputParser

from graph import State
from config import gemini_llm

from dotenv import load_dotenv
load_dotenv()

@tool
def get_language(code:str) -> str:
    
    """Using the code provided, the tool identifies the programming language."""
    
    try:
        lexer = guess_lexer(code)
        return f"The Programming language used here is {lexer.name}"
    
    except ClassNotFound:
        return "Programming Language not found!"

# @tool
# def code_review(language:str,code:str) -> str:
#     """
#         Using the programing language and the programing code snipet provided identify bugs,
#         performance issues, security risks,and style improvements.
#     """

#     prompt = f"You are a professional code reviewer who analyses the code and identify bugs,performance issues, security risks,and reports it in a professional and respected manner.Give the report in a string.\n PROGRAMMING LANGUAGE: {language}\n CODE: {code}"

#     response = gemini_llm.invoke(prompt)
#     return f"CODE REVIEW: {response}"

def Agent(question: str):
    agent = create_agent(
        model = gemini_llm,
        tools=[get_language],
        system_prompt="""
    You are an expert code reviewer.

    You MUST use the get_language tool before reviewing any code.
    Then review the code for:
    - Bugs
    - Performance issues
    - Security issues
    - Style improvements
    - Best practices
    """
    )
    response = agent.invoke({"messages": [{"role":"user","content": question}]})
    print(response["messages"][-1].content)

Agent("""def divide(a, b):
    return a / b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(divide(num1, num2))""")

