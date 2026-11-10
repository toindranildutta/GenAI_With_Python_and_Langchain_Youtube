from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.title("AskBuddy: AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    text = message ["text"]
    st.chat_message(role).markdown(text)

query = st.chat_input("Ask a Question")
if query:
    st.session_state.messages.append({"role": "user", "text": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.text)
    st.session_state.messages.append({"role": "ai", "text": res.text})


# while True:
#     query = input("User: ")

#     if query.lower() in ["quit", "exit"]:
#         print("Goodbye")
#         break

#     res = llm.invoke(query)
#     print("AI: ", res.text, "\n")