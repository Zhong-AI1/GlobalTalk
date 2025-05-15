import streamlit as st
import openai

# 設定OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "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"

st.title("我的生成式AI聊天機器人")

# 儲存對話訊息用
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "你是一個友善的助手。"}]

# 輸入框
user_input = st.text_input("請輸入你的問題：")

if user_input:
    # 把使用者輸入加到訊息串列
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 呼叫OpenAI的ChatCompletion
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        assistant_reply = response.choices[0].message["content"]

        # 把機器人回答加到訊息串列
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        st.error(f"發生錯誤: {e}")

# 顯示對話內容
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**你:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**機器人:** {msg['content']}")
