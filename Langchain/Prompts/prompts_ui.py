from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt

load_dotenv()
st.header("Research Tool")
st.write("aur gandu aa gye")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
paper_input = st.selectbox("research paper",["ALL FOR ONE","SOMETHING I GOT","UNIQUENESS"])
style_input = st.selectbox("style",["Happy","Sad"])
length_input = st.selectbox("length",["1 paragraph","5 paragraph"])


template = load_prompt('template.json')
#fill the placeholder




if st.button('Summarise'):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })
    st.write(result.content)
