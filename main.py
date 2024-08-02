import streamlit as st
from Helper import get_qa_chain, create_vector

st.title("Vehicle and Traffic Rules 🚦🚐 ")
st.title("SafetySensei Techno-Bot 🤖🔥")
#image = "1.jpg"
#st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])