import streamlit as st
import os
from PIL import Image, ImageEnhance

# Caminho do diretório (modifique para o caminho correto)
image_directory = "C:/caminho/para/sua/pasta"  # Exemplo no Windows
# image_directory = "/caminho/para/sua/pasta"  # Exemplo no Linux/macOS

st.title("SamurAI - Visualizador de Imagens")

# Verifica se o diretório existe
if not os.path.exists(image_directory):
    st.error("Diretório não encontrado! Verifique o caminho.")
else:
    # Lista todas as imagens na pasta
    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

    if not image_files:
        st.warning("Nenhuma imagem encontrada na pasta.")
    else:
        # Criar um seletor de imagem na barra lateral
        selected_image = st.sidebar.selectbox("Escolha uma imagem", image_files)

        if selected_image:
            image_path = os.path.join(image_directory, selected_image)
            image = Image.open(image_path)

            # Barra lateral para edição da imagem
            with st.sidebar:
                st.header("Edição de Imagem")
                brightness = st.slider("Brilho", 0.5, 2.0, 1.0)
                contrast = st.slider("Contraste", 0.5, 2.0, 1.0)
                sharpness = st.slider("Nitidez", 0.5, 2.0, 1.0)

            # Aplicar ajustes
            edited_image = ImageEnhance.Brightness(image).enhance(brightness)
            edited_image = ImageEnhance.Contrast(edited_image).enhance(contrast)
            edited_image = ImageEnhance.Sharpness(edited_image).enhance(sharpness)

            # Exibir a imagem original e a editada
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption="Original", use_column_width=True)
            with col2:
                st.image(edited_image, caption="Editada", use_column_width=True)

            st.write(f"Exibindo: {selected_image}")
