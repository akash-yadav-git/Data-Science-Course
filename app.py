import streamlit as st
st.title("String App")
message=st.text_area("Enter some text")
button=st.button("Process text")

if button:
    st.write(message)
if st.sidebar.checkbox("show words"):
    words=message.split()
    st.write(words)
if st.checkbox("character count"):
    
    for char in message:
        st.write(f'{char}:{message.count(char)}')

   