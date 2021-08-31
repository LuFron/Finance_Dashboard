import streamlit as st

from MultiPage import MultiPage
from pages import data_upload

# Create instance
app=MultiPage()

# Title of page
st.title('Financial Dashboard')

# Add Pages
app.add_pages("Upload Data", data_upload.app)


# Run
app.run()
