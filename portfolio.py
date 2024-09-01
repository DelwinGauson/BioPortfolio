import streamlit as st

def show_portfolio():
    st.header("Portfolio")
    
    st.subheader("Project 1: Hello World")
    st.write("This project was built using Python and Streamlit.")
    st.code("""
    def cool_function():
        print("Hello, World!")
    """, language="python")
    
    st.subheader("Project 2: Ongoing Work")
    st.write("This project is currently in progress.")
    st.progress(75)
    
    st.subheader("Skills")
    st.write("""
    - Programming Languages: Python, Java, C
    - Web Development: HTML, CSS, JavaScript, Streamlit
    - Database Management: MySQL
    - Others: Git, PC Assembly
    """)

