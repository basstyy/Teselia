# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Pokémon")
st.badge("Región", color="red", icon=":material/chevron_right:")

# Sutítulo
st.header("Aquí encontrarás mi región favorita de pokémon", divider=True)
#imagen mas una descripción
st.image("teselia.png", caption="Mapa de la 5ta región, TESELIA/UNOVA")
#escritura
st.write(
"""
**Teselia mi región favorita** 
Teselia es una región que se destaca por varias razones, lo que la convierte en una de las mejores de la franquicia de Pokémon. Una de las cosas más notables es su banda sonora. La música de Teselia es muy variada y memorable, lo que la hace única. Cada ciudad, ruta y batalla tiene su propio tema musical que se adapta perfectamente al ambiente, haciendo que la experiencia de juego sea mucho más inmersiva.

Además de su música, la variedad de Pokémon es algo que realmente distingue a Teselia. Fue la primera región en introducir una Pokédex completamente nueva. Esto significó que los jugadores no se encontraban con los mismos Pokémon de siempre al principio de la aventura, lo que le dio un aire de frescura y sorpresa. Esta decisión creativa hizo que explorar la región y descubrir nuevas especies fuera muy emocionante y gratificante.
"""
    )