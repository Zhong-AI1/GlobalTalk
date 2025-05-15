import streamlit as st
import openai

openai.api_key = "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鑰"

st.title("簡易測試")

if st.button("跟AI打招呼"):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "你好"}]
    )
    st.write(response.choices[0].message.content)
