import streamlit as st
import pandas as pd

def show_contact():
    st.header("Contact Me")
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Submit"):
        st.success(f"Thank you, {name}! Your message has been sent.")
    
    st.write("Or connect with me on social media:")
    st.markdown("[Facebook](https://www.facebook.com) | [GitHub](https://www.github.com)")
    
    map_data = pd.DataFrame({
        'lat': [10.252701],  
        'lon': [123.854912]
    })
    st.map(map_data)
