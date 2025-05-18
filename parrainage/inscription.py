import streamlit as st
from db import get_connection
import bcrypt

def inscription():
    st.title("📝 Inscription")

    # Liste des départements
    departements = [
        "Département Génie Informatique",
        "Département Génie Chimie et Biologie Appliquée",
        "Département Gestion",
        "Département Génie Civil"
    ]

    # Formulaire
    role = st.selectbox("Je suis :", ["Parrain", "Filleul"])
    numero_tel = st.text_input("📱 Numéro de téléphone", max_chars=9)
    nom = st.text_input("👤 Nom")
    prenom = st.text_input("🧍 Prénom")
    departement = st.selectbox("🏫 Département", departements)
    mot_de_passe = st.text_input("🔒 Mot de passe", type="password")

    if st.button("✅ S'inscrire", key="btn_inscription_submit"):

        # Validation
        if not all([numero_tel, nom, prenom, departement, mot_de_passe]):
            st.warning("⚠️ Veuillez remplir tous les champs.")
            return

        if not numero_tel.isdigit() or len(numero_tel) != 9:
            st.warning("⚠️ Le numéro doit contenir exactement 9 chiffres.")
            return

        if not (numero_tel.startswith("77") or numero_tel.startswith("76") or numero_tel.startswith("70") or numero_tel.startswith("75")):
            st.warning("⚠️ Le numéro doit commencer par 77, 76, 70 ou 75.")
            return

        try:
            # Connexion DB
            conn = get_connection()
            cursor = conn.cursor()

            table = "parains" if role == "Parrain" else "filleuls"

            # Vérifier si le numéro existe déjà
            cursor.execute(f"SELECT 1 FROM {table} WHERE numero_tel = %s", (numero_tel,))
            if cursor.fetchone():
                st.error(f"❌ Ce {role.lower()} est déjà inscrit avec ce numéro.")
                return

            # Hash du mot de passe
            hashed_pwd = bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())

            # Insertion
            cursor.execute(f"""
                INSERT INTO {table} (numero_tel, nom, prenom, departement, mot_de_passe)
                VALUES (%s, %s, %s, %s, %s)
            """, (numero_tel, nom, prenom, departement, hashed_pwd))
            conn.commit()

            st.success(f"🎉 {role} inscrit avec succès ! Vous pouvez maintenant vous connecter.")
            st.balloons()
            st.experimental_rerun()

        except Exception as e:
            st.error(f"❌ Erreur lors de l'inscription : {e}")

        finally:
            cursor.close()
            conn.close()
