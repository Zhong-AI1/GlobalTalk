import streamlit as st
from openai import OpenAI
import os

# 從環境變數讀取 API Key（請先設定 OPENAI_API_KEY）
client = OpenAI()

st.title("簡易生成式AI聊天機器人")

user_input = st.text_input("請輸入你的問題：")

if st.button("送出"):
    if user_input.strip() == "":
        st.warning("請輸入問題")
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            st.markdown(f"**機器人回答:** {answer}")
        except Exception as e:
            st.error(f"發生錯誤: {e}")
