import streamlit as st
import pandas as pd

def show_autobiography():
    st.header("Autobiography")
    
    st.markdown(open("autobiography.md").read())

    with st.expander("Read more about my hobbies"):
        st.write("I also enjoy biking.")
        
    map_data = pd.DataFrame({
        'lat': [10.252701],  
        'lon': [123.854912] 
    })
    st.map(map_data)
