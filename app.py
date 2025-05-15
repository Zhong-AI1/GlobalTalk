import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入 .env 裡的 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI 聊天助手")

user_input = st.text_input("你想問什麼？")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 或 gpt-4
        messages=[
            {"role": "system", "content": "你是一位親切又專業的 AI 助手。"},
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response.choices[0].message.content)
