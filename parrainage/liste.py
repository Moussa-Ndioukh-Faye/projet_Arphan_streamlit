import streamlit as st
from db import get_connection

def afficher_listes():
    st.subheader("📜 Liste des utilisateurs inscrits")

    conn = get_connection()
    cursor = conn.cursor()

    choix = st.selectbox("Choisissez la liste à afficher", ["Parrains", "Filleuls"])

    if choix == "Parrains":
        cursor.execute("SELECT numero_tel, nom, prenom, departement FROM parains")
        users = cursor.fetchall()
        st.markdown("### 🧑‍🎓 Parrains")
    else:
        cursor.execute("SELECT numero_tel, nom, prenom, departement FROM filleuls")
        users = cursor.fetchall()
        st.markdown("### 👶 Filleuls")

    if users:
        # Affichage dans un tableau Streamlit
        import pandas as pd
        df = pd.DataFrame(users, columns=["Téléphone", "Nom", "Prénom", "Département"])
        st.table(df)
    else:
        st.info("Aucun utilisateur trouvé.")

    cursor.close()
    conn.close()

