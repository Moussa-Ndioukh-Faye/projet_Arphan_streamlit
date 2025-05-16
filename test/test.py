import streamlit as st
import random

# Initialisation de la session (exécuté une seule fois)
if "a" not in st.session_state:
    st.session_state.a = random.getrandbits(10)
    st.session_state.b = random.getrandbits(10)
    while st.session_state.b <= st.session_state.a:
        st.session_state.b = random.getrandbits(10)
    st.session_state.nombre_mystere = random.randint(st.session_state.a, st.session_state.b)
    st.session_state.message = ""

st.title("🎯 Jeu du Nombre Mystère")
st.write(f"Devinez le nombre mystère entre *{st.session_state.a}* et *{st.session_state.b}*.")

# Saisie de l'utilisateur
devine = st.number_input("Entrez votre proposition :", step=1, format="%d")

# Bouton de validation
if st.button("Valider ma proposition"):
    try:
        if int(devine) == st.session_state.nombre_mystere:
            st.success("Bravo ! Vous avez trouvé le nombre mystère ! 🎉")
        elif int(devine) < st.session_state.nombre_mystere:
            st.warning("C'est plus grand ! Essayez encore.")
        else:
            st.warning("C'est plus petit ! Essayez encore.")
    except ValueError:
        st.error("Veuillez entrer un nombre valide.")