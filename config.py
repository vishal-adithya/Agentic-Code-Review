from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0
)
response  = gemini_llm.invoke("test!")
print(response)