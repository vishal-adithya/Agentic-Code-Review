from langchain.agents import create_agent
from langchain.tools import tool
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

from graph import State
from config import gemini_llm

@tool
def get_language(state:State) -> State:
    
    """Using the code provided identifies the programming language."""
    
    try:
        lexer = guess_lexer(state["code"])
        return {"language" : lexer.name}
    
    except ClassNotFound:
        return {"language" : "Unidentified Language!"}

@tool
def code_reveiew(state:State) -> State:
    """
        Using the programing language and the programing code snipet provided identify bugs,
        performance issues, security risks,and style improvements.
    """

    prompt = f"You are a professional code reviewer who analyses the code and identify bugs,performance issues, security risks,and reports it in a professional and respected manner.Give the report in a string.\n PROGAMMING LANGUAGE: {state["language"]}\n CODE: {state["code"]}"

    response = gemini_llm.invoke(prompt)
    print(response)
    return {"code_review": response}