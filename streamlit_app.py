import streamlit as st

# Configurar la página
st.set_page_config(page_title="Yeeezy", page_icon="🚀", layout="wide")

# Estilos personalizados
st.markdown(
    """
    <style>
    .main {
        background-color: #1E1E1E;
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    .title {
        text-align: center;
        font-size: 40px;
        color: #00ff99;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título con mejor diseño
st.markdown("<div class='title'>🚀 Bienvenido a Yeeezy</div>", unsafe_allow_html=True)

st.write(
    "¡Comienza a construir tu aplicación! Para obtener ayuda e inspiración, visita [Streamlit Docs](https://docs.streamlit.io/)."
)

st.sidebar.title("🔧 Configuración")
st.sidebar.write("Ajusta las opciones de tu app aquí.")
