import streamlit as st
import openai
from dotenv import load_dotenv
import os

# 載入 .env 中的 API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="我的 AI 聊天機器人")

st.title("🤖 我的生成式 AI 聊天機器人")

# 輸入文字
user_input = st.text_input("請輸入訊息：")

if user_input:
    with st.spinner("AI 正在回覆中..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content
            st.success("AI 回覆：")
            st.write(reply)
        except Exception as e:
            st.error(f"發生錯誤：{e}")
