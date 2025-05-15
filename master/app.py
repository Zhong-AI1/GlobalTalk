import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# 載入 .env 檔裡的環境變數
load_dotenv()

client = OpenAI(api_key="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")

# 從環境變數讀取 API Key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("未設定 OPENAI_API_KEY，請確認 .env 檔或環境變數是否正確。")
    st.stop()

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=api_key)

st.title("簡易AI聊天機器人")

user_input = st.text_input("請輸入你的問題：")

if st.button("送出"):
    if not user_input.strip():
        st.warning("請輸入問題後再送出。")
    else:
        try:
            # 呼叫 Chat Completion API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            answer = response.choices[0].message.content
            st.markdown(f"**機器人回答：** {answer}")
        except Exception as e:
            st.error(f"發生錯誤：{e}")
