import streamlit as st
import zipfile
import os
from io import BytesIO
from PIL import Image, ImageEnhance

# Definindo o tema escuro
st.set_page_config(page_title="SamurAI", page_icon="🏯", layout="wide")

st.title("SamurAI - Upload de Pasta")

# Barra lateral com opções e edição de imagem
with st.sidebar:
    st.header("Opções")
    show_files = st.checkbox("Mostrar arquivos extraídos")
    selected_file = None

uploaded_file = st.file_uploader("Faça upload de um arquivo ZIP contendo a pasta", type=["zip"])

if uploaded_file is not None:
    st.write("Arquivo recebido:", uploaded_file.name)
    
    # Lendo o arquivo ZIP na memória
    with zipfile.ZipFile(BytesIO(uploaded_file.read()), "r") as zip_ref:
        extract_path = "uploaded_folder"
        zip_ref.extractall(extract_path)  # Extrai os arquivos para uma pasta temporária
        
        # Listar os arquivos extraídos
        image_files = [f for f in os.listdir(extract_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

        if show_files:
            st.sidebar.write("Arquivos extraídos:")
            for file in image_files:
                st.sidebar.write(file)

        # Permitir que o usuário selecione um arquivo
        if image_files:
            selected_file = st.sidebar.selectbox("Escolha uma imagem", image_files)

        if selected_file:
            image_path = os.path.join(extract_path, selected_file)
            image = Image.open(image_path)

            # Barra lateral para edição da imagem
            with st.sidebar:
                st.header("Edição de Imagem")
                brightness = st.slider("Brilho", 0.5, 2.0, 1.0)
                contrast = st.slider("Contraste", 0.5, 2.0, 1.0)
                sharpness = st.slider("Nitidez", 0.5, 2.0, 1.0)

            # Aplicar ajustes na imagem
            edited_image = ImageEnhance.Brightness(image).enhance(brightness)
            edited_image = ImageEnhance.Contrast(edited_image).enhance(contrast)
            edited_image = ImageEnhance.Sharpness(edited_image).enhance(sharpness)

            # Exibir imagens lado a lado
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption="Original", use_container_width=True)
            with col2:
                st.image(edited_image, caption="Editada", use_container_width=True)
