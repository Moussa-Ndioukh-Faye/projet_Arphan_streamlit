import streamlit as st
import mysql.connector

def connexion():
    st.title("Connexion")
    numero = st.text_input("Téléphone")
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
    
        st.success("Connexion réussie !")