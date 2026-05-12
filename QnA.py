import streamlit as st
import google.generativeai as genai

genai.configure(api_key="your gemini api key")
model=genai.GenerativeModel("gemini-pro")

def get_response(input):
    response=model.generate_content(input)
    return response.text


st.header("Gemini QnA bot")
st.set_page_config(page_title="Gemini QnA bot")
text=st.text_input ("What do you want to do?",key="text")
submit=st.button("Get response")

if submit:
    response=get_response(text)
    st.subheader("your response")
    st.write(response)


