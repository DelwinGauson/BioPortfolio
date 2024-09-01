import streamlit as st
from portfolio import show_portfolio
from autobiography import show_autobiography
from contact import show_contact
import sidebar

st.set_page_config(page_title="Gauson Streamlit", layout="wide")

def main():
    
    page = sidebar.render_sidebar()
    
    st.title("Welcome to My Autobiography and Portfolio")
    
    if page == "Autobiography":
        show_autobiography()
    elif page == "Portfolio":
        show_portfolio()
    elif page == "Contact":
        show_contact()

if __name__ == "__main__":
    main()
