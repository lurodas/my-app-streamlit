import streamlit as st

st.title("Convertidor de Texto a Mayúsculas")

# Caja de texto para ingresar datos
texto_usuario = st.text_input("Escribe tu texto aquí:", "")

# Procesamiento del texto
if texto_usuario:
    texto_mayusculas = texto_usuario.upper()
else:
    texto_mayusculas = ""

# Caja de texto para mostrar el resultado
st.text_area("Texto procesado (Mayúsculas):", value=texto_mayusculas, height=100, disabled=True)
