import streamlit as st
import zipfile
import os
from io import BytesIO

st.title("SamurAI - Upload de Pasta")

uploaded_file = st.file_uploader("Faça upload de um arquivo ZIP contendo a pasta", type=["zip"])

if uploaded_file is not None:
    st.write("Arquivo recebido:", uploaded_file.name)
    
    # Lendo o arquivo ZIP na memória
    with zipfile.ZipFile(BytesIO(uploaded_file.read()), "r") as zip_ref:
        extract_path = "uploaded_folder"
        zip_ref.extractall(extract_path)  # Extrai os arquivos para uma pasta temporária
        
        # Lista os arquivos extraídos
        st.write("Arquivos extraídos:")
        for root, dirs, files in os.walk(extract_path):
            for file in files:
                st.write(os.path.join(root, file))

