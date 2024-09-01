import streamlit as st

def show_portfolio():
    st.header("Portfolio")
    
    st.subheader("Project 1: Cebu City Family Records API")
    st.write("This project was built using C# and TSQL.")
    st.write("This project delivers capabilities that allow for the efficient management of information regarding Families residing in a certain Barangay. It ensures that a Barangay can maintain track of the Details of each Family Member and the population.")
    st.image("images/erdproj.png", caption="Cebu City Family Records ERD", use_column_width=True)
    
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

