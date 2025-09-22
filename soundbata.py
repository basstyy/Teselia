# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
st.header("Teselia, soundtrack y más", divider=True)
#como poner video
st.video("https://youtu.be/qZnm1A8XP5M?si=2kcZY2dI9H3vI2nR")
#escritura antes del tema principal
st.write("** Aquí el mejor tema de este increible y maravilloso, gloriosa obra de arte ** " )
#escritura tema principal
st.write(
"""El tema de batalla de líder de gimnasio de Pokémon Negro y Blanco, conocido como "Battle! (Gym Leader)" en el juego, es a menudo considerado uno de los mejores de toda la franquicia por varias razones.

Este tema se destaca por su carácter dinámico y evolutivo. La música no se queda estática durante la batalla, sino que se transforma a medida que esta avanza. La primera parte del tema es enérgica y electrónica, ideal para el comienzo de un desafío. Sin embargo, lo que realmente lo hace sobresaliente es cuando el líder de gimnasio saca a su último Pokémon. En ese momento, la canción se intensifica, agregando una orquesta con instrumentos de viento y batería que elevan la tensión de la batalla a un nivel épico.

Esta transición crea una sensación de urgencia y dramatismo, haciendo que el jugador se sienta más involucrado en el clímax de la pelea. Es una banda sonora que no solo acompaña la acción, sino que se convierte en una parte integral de la experiencia, haciendo que cada batalla de gimnasio en Teselia sea memorable y emocionante.

"""
    )
#escritura mas abajo 
st.markdown(
"""
Batallas Dinámicas y Estratégicas
Las batallas en este juego son muy atractivas porque introducen varios elementos nuevos que fomentan la estrategia. Por un lado, tenemos las batallas triples y rotatorias, que obligan al jugador a pensar de forma diferente sobre la posición de sus Pokémon y cómo los movimientos pueden afectar a múltiples oponentes o cambiar de objetivo en un instante.

Además, la introducción de nuevos Pokémon con habilidades y movimientos únicos hizo que el metajuego competitivo se renovara por completo. La región de Teselia trajo Pokémon como Haxorus, Volcarona y Excadrill, que se volvieron muy populares por su poder y versatilidad. Esto hizo que las batallas no se sintieran repetitivas, incluso contra entrenadores no jugables.

Una Pokédex Completamente Nueva
La Pokédex de Teselia es, sin duda, una de las más especiales y elogiadas de toda la serie. A diferencia de otros juegos, Pokémon Negro y Blanco no incluye a ningún Pokémon de las generaciones anteriores en su Pokédex regional original. Esto significa que, desde el inicio del juego, cada encuentro con un Pokémon es una sorpresa y una nueva experiencia.

Esta decisión refrescante obligó a los jugadores a explorar y descubrir las 156 nuevas especies (la mayor cantidad en una sola generación), lo que le dio al juego una sensación de novedad y aventura que no se había visto desde la primera generación. Esta Pokédex no solo es grande, sino que también está llena de Pokémon con diseños creativos y únicos, lo que contribuye a que el mundo se sienta vivo y lleno de misterio.
""")


st.image("sprites.png", caption="Combate en el juego")