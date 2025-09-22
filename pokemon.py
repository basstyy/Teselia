# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Pokémon",
    page_icon=":no_entry:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo
st.logo(
    "pokebola.png",
)
#para iniciar las paginas
pg = st.navigation(["Homepage.py" , "Regiones_pokemon.py", "soundbata.py", "amigos.py" , "iniciales.py" , "Legendarios.py" , "Quienes_somos.py"])
pg.run()
