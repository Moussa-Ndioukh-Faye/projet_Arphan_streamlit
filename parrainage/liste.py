import streamlit as st
from db import get_connection

def afficher_listes():
    st.header("Listes des inscrits")

    conn = get_connection()
    cursor = conn.cursor()

    # --- Parrains ---
    st.subheader("👨‍🏫 Parrains")
    try:
        cursor.execute("SELECT nom, prenom, numero_tel, departement FROM parains")
        parrains = cursor.fetchall()

        if parrains:
            for p in parrains:
                st.write(f"👤 {p[0]} {p[1]} | 📱 {p[2]} | 📍 {p[3]}")
        else:
            st.info("Aucun parrain inscrit pour le moment.")
    except Exception as e:
        st.error(f"Erreur : {e}")

    st.markdown("---")

    # --- Filleuls ---
    st.subheader("🧑‍🎓 Filleuls")
    try:
        cursor.execute("SELECT nom, prenom, numero_tel, departement FROM filleuls")
        filleuls = cursor.fetchall()

        if filleuls:
            for f in filleuls:
                st.write(f"👤 {f[0]} {f[1]} | 📱 {f[2]} | 📍 {f[3]}")
        else:
            st.info("Aucun filleul inscrit pour le moment.")
    except Exception as e:
        st.error(f"Erreur : {e}")

    cursor.close()
    conn.close()
