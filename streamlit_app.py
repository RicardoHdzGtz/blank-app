import streamlit as st 

# Configurar la página
st.set_page_config(page_title="Yeeezy", page_icon="🎵", layout="wide")

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
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #bbbbbb;
        margin-top: -10px;
    }
    .info-box {
        background-color: #222;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        color: white;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título y subtítulo
st.markdown("<div class='title'>Bienvenido a Yeeezy</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Página de datos sobre música</div>", unsafe_allow_html=True)

# Datos interesantes sobre Oasis
dato_oasis_1 = """
🎸 ¿Sabías que...?  
Cuando Oasis grabó Wonderwall, Noel Gallagher originalmente quería que la canción fuera cantada por él,  
pero al final dejó que su hermano Liam la interpretara. Hoy es una de las canciones más icónicas de la banda.  
"""

dato_oasis_2 = """
🎤 Otro dato curioso: 
En 1994, Oasis fue vetado de los Estados Unidos después de que sus miembros fueran detenidos en el aeropuerto  
por comportamiento indebido. A pesar de esto, la banda se convirtió en un fenómeno global.  
"""

# Mostrar los datos
st.markdown(f"<div class='info-box'>{dato_oasis_1}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='info-box'>{dato_oasis_2}</div>", unsafe_allow_html=True)
