import streamlit as st
from db import get_connection

def connexion():
    st.header("Connexion")

    role = st.selectbox("Connexion en tant que :", ["Parrain", "Filleul"])
    numero_tel = st.text_input("Numéro de téléphone")
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        conn = get_connection()
        cursor = conn.cursor()

        table = "parains" if role == "Parrain" else "filleuls"
        cursor.execute(f"""
            SELECT * FROM {table} WHERE numero_tel = %s AND mot_de_passe = %s
        """, (numero_tel, mot_de_passe))
        
        user = cursor.fetchone()
        conn.close()

        if user:
            st.success(f"{role} connecté avec succès !")
            st.write("Bienvenue,", user[2])  # prénom
        else:
            st.error("Numéro ou mot de passe incorrect.")

