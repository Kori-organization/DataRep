import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.prompts.student_system_prompt import STUDENT_SYSTEM_PROMPT
from app.prompts.professor_system_prompt import PROFESSOR_SYSTEM_PROMPT
from app.prompts.student_user_prompt import STUDENT_USER_PROMPT
from app.prompts.professor_user_prompt import PROFESSOR_USER_PROMPT

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    top_p=0.95,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

student_prompt = ChatPromptTemplate.from_messages([
    ("system", STUDENT_SYSTEM_PROMPT),
    ("human", STUDENT_USER_PROMPT)
])

professor_prompt = ChatPromptTemplate.from_messages([
    ("system", PROFESSOR_SYSTEM_PROMPT),
    ("human", PROFESSOR_USER_PROMPT)
])

student_chain = student_prompt | llm | StrOutputParser()
professor_chain = professor_prompt | llm | StrOutputParser()