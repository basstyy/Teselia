# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("¿Quienes somos?")
st.badge("Poke-data", color="blue", icon=":material/chevron_right:")

# Sutítulo
st.header("", divider=True)
#imagen
st.image("portada.jpg", caption="Portada del juego de esta región")
#escritura
st.write("""Bienvenidos a nuestra Poké-Data.

En esta página, no somos solo un sitio de fans más. Somos el recurso esencial para cualquier entrenador Pokémon que quiera ir más allá de la simple aventura. Aquí nos dedicamos a la data y los detalles que hacen que el mundo Pokémon sea tan profundo y fascinante.
Acá encontraremos un poco de información de esta region y porque es una de mi region favorita al igual que mucha cantidad de gente, luego encontraras un poco de información sobre una de las mejores canciones de este juego (ciudad fayenza y gym) y destacando porque este tiene una de las mejores batallas en el universo de pokemon, aparte de una de las mejores animaciones para la época.
luego encontraremos un poco de información sobre los amigos de Ash Ketchum en esta región destacando a Iris que luego en pokémon negro 2 se hace la lider del alto mando.
luego se menciona de los iniciales de esta región, cualidades y evoluciones de estas para ir finalizando con los legendarios de esta región y el porque estos pueden ser de lo mejorcito de la franquicia.
Esperamos profundamente que les guste y disfruten. ¡Atrapalos Ya!""")

#como poner video
st.audio("C:/Users/user_/Downloads/pokemon-atrapalos-ya-latino-oscar-roa-full-128-ytshorts.savetube.me.mp3")