import streamlit as st
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Função para selecionar a pasta
def select_folder():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    folder_selected = filedialog.askdirectory()  # Abre o seletor de pasta
    return folder_selected

# Botão para selecionar a pasta
if st.button("Selecionar Pasta"):
    folder_path = select_folder()
    st.session_state.folder_path = folder_path  # Salva na sessão

# Exibir o caminho da pasta
folder_path = st.session_state.get("folder_path", "")

if folder_path:
    st.success(f"Pasta selecionada: {folder_path}")

    # Listar imagens da pasta
    def load_images(folder):
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    images = load_images(folder_path)

    # Exibir miniaturas
    cols = st.columns(4)
    for i, img_path in enumerate(images):
        with cols[i % 4]:
            img = Image.open(img_path)
            img.thumbnail((150, 150))
            if st.button(f"🔍 {os.path.basename(img_path)}", key=f"btn_{i}"):
                st.session_state.selected_image = img_path

    # Exibir imagem ampliada
    if st.session_state.get("selected_image"):
        st.image(st.session_state.selected_image, caption="Imagem Ampliada", use_column_width=True)
        if st.button("Fechar"):
            st.session_state.selected_image = None
else:
    st.warning("Selecione uma pasta para visualizar as imagens.")
