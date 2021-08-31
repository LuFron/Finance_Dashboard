"""
    USe to define a class to manage multiple page on streamlit
"""

# Import streamlit
import streamlit as st

# Class definition
class MultiPage:

    def __init__(self) -> None:
        self.pages = []

    def add_pages(self, title, func) -> None:
        """ Class Mehod to Add pages to the project"""
        self.pages.append({
            'title': title,
            'function': func
        })

    def run(self):
        page = st.sidebar.selectbox('Page Navigation', self.pages, format_func=lambda page: page['title'])

        # run app function
        page['function']()
