import streamlit as st
def inscription():
    st.title("Inscription")
    role = st.selectbox("Je suis :", ["Parrain", "Filleul"])
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    numero = st.text_input("Téléphone")
    departement = st.text_input("Département")
    mdp = st.text_input("Mot de passe", type="password")

    if st.button("S'inscrire"):
        st.success(f"Inscription enregistrée pour {nom} {prenom} ({role})")
