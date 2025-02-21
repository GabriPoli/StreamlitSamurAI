import streamlit as st
import pandas as pd
from io import StringIO

st.title("SamurAI")

uploaded_files = st.file_uploader(
    "Escolha a pasta que deseja", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
