from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
st.write("API Key 前10碼:", api_key[:10] if api_key else "沒有讀到金鑰")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("請先在 .env 設定 OPENAI_API_KEY")
else:
    client = OpenAI(api_key=api_key)

    st.title("簡易測試")

    if st.button("跟AI打招呼"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "你好"}]
        )
        st.write(response.choices[0].message.content)
