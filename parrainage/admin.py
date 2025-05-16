import streamlit as st
from db import get_connection
import mysql.connector

def admin():
    st.header("Espace Administrateur")

    mot_de_passe_admin = st.text_input("Mot de passe admin", type="password")

    if mot_de_passe_admin != "admin123":
        st.warning("Veuillez entrer le mot de passe admin.")
        return

    st.success("Accès admin accordé ✅")

    conn = get_connection()
    cursor = conn.cursor()

    # Affichage des parrains
    st.subheader("Liste des parrains")
    cursor.execute("SELECT numero_tel, nom, prenom, departement FROM parains")
    parrains = cursor.fetchall()
    for p in parrains:
        st.write(f"📱 {p[0]} | 👤 {p[1]} {p[2]} | 📍 {p[3]}")

    # Affichage des filleuls
    st.subheader("Liste des filleuls")
    cursor.execute("SELECT numero_tel, nom, prenom, departement FROM filleuls")
    filleuls = cursor.fetchall()
    for f in filleuls:
        st.write(f"📱 {f[0]} |  {f[1]} {f[2]} | 📍 {f[3]}")

    cursor.close()
    conn.close()
