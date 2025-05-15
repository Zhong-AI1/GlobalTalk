import streamlit as st
import openai
from dotenv import load_dotenv
import os

# 載入環境變數（.env）
load_dotenv()

# 設定 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("我的生成式AI聊天機器人")

if "messages" not in st.session_state:
    # 初始對話訊息，角色設定系統提示
    st.session_state.messages = [
        {"role": "system", "content": "你是一個友善且樂於助人的聊天機器人。"}
    ]

# 輸入欄位
user_input = st.text_input("請輸入你的問題：", key="input")

def generate_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 或使用 gpt-4（需API權限）
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"發生錯誤: {e}"

if user_input:
    # 把使用者訊息加入對話紀錄
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 呼叫 OpenAI API 取得回應
    bot_response = generate_response(st.session_state.messages)

    # 把機器人回覆加入對話紀錄
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# 顯示聊天記錄，最新訊息在下面
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**你:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**機器人:** {msg['content']}")
