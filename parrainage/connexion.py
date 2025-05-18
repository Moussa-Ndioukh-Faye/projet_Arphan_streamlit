import streamlit as st
from db import get_connection
import bcrypt

def connexion():
    st.header("🔐 Connexion")

    role = st.selectbox("Connectez-vous en tant que :", ["Parrain", "Filleul", "Admin"])
    numero_tel = st.text_input("Numéro de téléphone", max_chars=9)
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if not numero_tel or not mot_de_passe:
            st.warning("Veuillez remplir tous les champs.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        if role == "Admin":
            cursor.execute("SELECT mot_de_passe FROM admins WHERE numero_tel = %s", (numero_tel,))
            result = cursor.fetchone()

            if result and result[0]:
                mot_de_passe_hache = result[0]
                
                try:
                    if bcrypt.checkpw(mot_de_passe.encode('utf-8'), mot_de_passe_hache.encode('utf-8')):
                        st.success("Connexion admin réussie ✅")
                        st.session_state.connecte = True
                        st.session_state.role = "admin"
                        cursor.close()
                        conn.close()
                        return
                    else:
                        st.error("Mot de passe incorrect.")
                except ValueError as e:
                    st.error(f"Erreur : le hash est invalide.\nDétails : {e}")
            else:
                st.error("Numéro admin inconnu.")

            cursor.close()
            conn.close()
            return

        # Utilisateur Parrain ou Filleul
        table = "parains" if role == "Parrain" else "filleuls"
        cursor.execute(f"SELECT nom, mot_de_passe FROM {table} WHERE numero_tel = %s", (numero_tel,))
        result = cursor.fetchone()

        if result and result[1]:
            nom, mot_de_passe_hache = result
            try:
                if bcrypt.checkpw(mot_de_passe.encode('utf-8'), mot_de_passe_hache.encode('utf-8')):
                    st.success(f"Bienvenue {nom} 🎉")
                    st.session_state.connecte = True
                    st.session_state.role = role.lower()
                else:
                    st.error("Mot de passe incorrect.")
            except ValueError:
                st.error("Le mot de passe stocké est invalide (hash corrompu).")
        else:
            st.error("Numéro inconnu.")

        cursor.close()
        conn.close()
