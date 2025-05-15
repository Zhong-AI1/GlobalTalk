from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 讀取 .env 變數（本地環境用）

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("沒有找到 OPENAI_API_KEY，請設定環境變數！")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("簡易測試")

if st.button("跟AI打招呼"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "你好"}]
    )
    st.write(response.choices[0].message.content)
