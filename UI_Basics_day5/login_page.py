import streamlit as st 
st.set_page_config(page_title="Text Input Demo")
st.title("Login Page")
name = st.text_input("Enter your name:",placeholder="e.g.sushi")
st.write(f"Hello,{name}!")

secret = st.text_input("Enter your password:",type="password")
st.write(f"your password has {len(secret)} characters.")
st.write(f"your password as atleast %,#,8 characters.")

comments=st.text_area("Any additional comments?",height=150)
st.write(f"your wrote {len(comments)} characters.")
if st.button("submit"):
    st.write("you clicked to submit!")