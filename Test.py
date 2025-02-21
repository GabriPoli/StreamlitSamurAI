import streamlit as st
import zipfile
import os
from io import BytesIO
from PIL import Image, ImageEnhance

st.title("SamurAI - Upload de Pasta")

# Barra lateral com controles de edição de imagem
with st.sidebar:
    st.header("Opções")
    show_files = st.checkbox("Mostrar arquivos extraídos")
    st.header("Edição de Imagem")
    brightness = st.slider("Brilho", 0.5, 2.0, 1.0)
    contrast = st.slider("Contraste", 0.5, 2.0, 1.0)
    sharpness = st.slider("Nitidez", 0.5, 2.0, 1.0)

uploaded_file = st.file_uploader("Faça upload de um arquivo ZIP contendo a pasta", type=["zip"])

if uploaded_file is not None:
    st.write("Arquivo recebido:", uploaded_file.name)
    
    # Lendo o arquivo ZIP na memória
    with zipfile.ZipFile(BytesIO(uploaded_file.read()), "r") as zip_ref:
        extract_path = "uploaded_folder"
        zip_ref.extractall(extract_path)  # Extrai os arquivos para uma pasta temporária
        
        # Lista os arquivos extraídos se o usuário marcar a opção na barra lateral
        if show_files:
            st.sidebar.write("Arquivos extraídos:")
            for root, dirs, files in os.walk(extract_path):
                for file in files:
                    st.sidebar.write(os.path.join(root, file))

        # Exibir e editar a primeira imagem encontrada no ZIP
        image_files = [f for f in os.listdir(extract_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

        if image_files:
            image_path = os.path.join(extract_path, image_files[0])
            image = Image.open(image_path)

            # Aplicar os ajustes de edição
            image = ImageEnhance.Brightness(image).enhance(brightness)
            image = ImageEnhance.Contrast(image).enhance(contrast)
            image = ImageEnhance.Sharpness(image).enhance(sharpness)

            # Exibir a imagem original e a editada
            col1, col2 = st.columns(2)
            with col1:
                st.image(Image.open(image_path), caption="Original", use_column_width=True)
            with col2:
                st.image(image, caption="Editada", use_column_width=True)
