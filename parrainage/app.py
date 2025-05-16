import streamlit as st
from inscription import inscription
from connexion import connexion
from admin import admin
from liste import afficher_listes
from matching import correspondance


def main():
    st.set_page_config(page_title="Site de Parrainage", page_icon="🤝", layout="centered")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choisissez une page", [
        "Accueil",
        "Inscription",
        "Connexion",
        "Admin",
        "Listes",
        "Matching"
    ])

    if page == "Accueil":
        st.title("Bienvenue sur le site de parrainage parrainage de ESP")
        st.markdown("Ce site permet aux **parrains** et **filleuls** de s'inscrire, se connecter et d'être mis en relation automatiquement.")

    elif page == "Inscription":
        inscription()

    elif page == "Connexion":
        connexion()

    elif page == "Admin":
        admin()

    elif page == "Listes":
        afficher_listes()

    elif page == "Matching":
        correspondance()

if __name__ == "__main__":
    main()
