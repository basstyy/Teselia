# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Amigos de Ash")
st.badge("Amigos", color="blue", icon=":material/chevron_right:")

# Sutítulo
st.header("", divider=True)
#imagen
st.image("amigos.webp", caption="Amigos de Ash Ketchum")
#escritura
st.write("""Iris
Iris es una entrenadora que sueña con convertirse en una Maestra Dragón. Es una joven vivaz, audaz y con un gran espíritu aventurero. Al principio, a menudo llama a Ash un "niño" (o "little kid" en el original) porque considera que es inmaduro o que sus decisiones no son las correctas. Sin embargo, con el tiempo, ella lo llega a respetar como un amigo y un entrenador.

Pokémon principal: Axew, un pequeño Pokémon dragón que siempre la acompaña fuera de su Poké Ball, y luego su potente Haxorus.

Habilidad especial: Es muy buena para entender y sentir las emociones de los Pokémon de tipo dragón.

Cilan
Cilan es uno de los líderes de gimnasio de la ciudad de Striaton y también un Connoisseur Pokémon. Un Connoisseur es alguien que puede juzgar la compatibilidad entre un Pokémon y su entrenador, así como la elegancia de su estilo de batalla. Es muy analítico y a menudo utiliza un lenguaje muy formal, evaluando todo con un estilo teatral y con frases como "¡Es hora de la evaluación!"

Pokémon principal: Su Pokémon más conocido es su Pansage.

Habilidad especial: Es un chef excepcional y siempre está dispuesto a preparar comidas deliciosas para el grupo. También es un experto en varios oficios, lo que lo convierte en un compañero de viaje muy útil.""")