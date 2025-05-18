import streamlit as st
from db import get_connection
import pandas as pd

def admin():
    st.header("🔐 Espace Administrateur")

    # Saisie du mot de passe admin
    mot_de_passe = st.text_input("Mot de passe admin :", type="password")
    if mot_de_passe != "admin123":
        st.info("Accès restreint. Entrez le mot de passe pour continuer.")
        return
    st.success("✅ Accès admin accordé")

    conn = get_connection()
    cursor = conn.cursor()

    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    # 🧭 Sélection du département
    cursor.execute("SELECT DISTINCT departement FROM parains UNION SELECT DISTINCT departement FROM filleuls")
    departements = [row[0] for row in cursor.fetchall()]
    departement_filtre = st.selectbox("📍 Filtrer par département", options=["Tous"] + departements)

    # Fonction de filtre SQL
    def where_dept(table):
        return f"WHERE departement = '{departement_filtre}'" if departement_filtre != "Tous" else ""

    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    # 👨 Liste des parrains
    st.subheader("👨 Parrains inscrits")
    cursor.execute(f"""
        SELECT numero_tel, nom, prenom, departement, date_inscription
        FROM parains {where_dept("parains")} ORDER BY date_inscription DESC
    """)
    parrains = cursor.fetchall()

    if parrains:
        df_parrains = pd.DataFrame(parrains, columns=["Téléphone", "Nom", "Prénom", "Département", "Date d'inscription"])
        st.dataframe(df_parrains)
    else:
        st.info("Aucun parrain trouvé.")

    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    # 🧒 Liste des filleuls
    st.subheader("🧒 Filleuls inscrits")
    cursor.execute(f"""
        SELECT numero_tel, nom, prenom, departement, date_inscription
        FROM filleuls {where_dept("filleuls")} ORDER BY date_inscription DESC
    """)
    filleuls = cursor.fetchall()

    if filleuls:
        df_filleuls = pd.DataFrame(filleuls, columns=["Téléphone", "Nom", "Prénom", "Département", "Date d'inscription"])
        st.dataframe(df_filleuls)
    else:
        st.info("Aucun filleul trouvé.")

    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    # 🗑️ Suppression d'un utilisateur
    st.subheader("🗑️ Supprimer un utilisateur")
    role = st.radio("Type d'utilisateur à supprimer :", ["Parrain", "Filleul"])
    tel_supprimer = st.text_input("Numéro de téléphone de l'utilisateur à supprimer")

    if st.button("Supprimer l'utilisateur"):
        if tel_supprimer:
            table = "parains" if role == "Parrain" else "filleuls"
            cursor.execute(f"DELETE FROM {table} WHERE numero_tel = %s", (tel_supprimer,))
            conn.commit()
            st.success(f"{role} avec le numéro {tel_supprimer} supprimé avec succès.")
        else:
            st.warning("Veuillez entrer un numéro de téléphone.")

    cursor.close()
    conn.close()
