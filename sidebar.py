import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar():
    with st.sidebar:
        selected = option_menu(
            "Menu",  
            ["Autobiography", "Portfolio", "Contact"], 
            icons=["book", "briefcase", "envelope"],  
            menu_icon="cast", 
            default_index=0,  
        )
    return selected