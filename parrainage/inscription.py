import streamlit as st
from db import get_connection

def inscription():
    st.title("📝 Inscription")

    role = st.selectbox("Je suis :", ["Parrain", "Filleul"])
    numero_tel = st.text_input(" Numéro de téléphone, max")
    nom = st.text_input(" Nom")
    prenom = st.text_input(" Prénom")
    departement = st.text_input("Département")
    mot_de_passe = st.text_input("🔒 Mot de passe", type="password")

    if st.button("✅ S'inscrire"):
        # Vérifier que tous les champs sont remplis
        if not all([numero_tel, nom, prenom, departement, mot_de_passe]):
            st.warning("⚠️ Veuillez remplir tous les champs.")
            return

        if not numero_tel.isdigit():
            st.warning("📵 Le numéro de téléphone doit contenir uniquement des chiffres.")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            if role == "Parrain":
                cursor.execute("SELECT * FROM parains WHERE numero_tel = %s", (numero_tel,))
                if cursor.fetchone():
                    st.error("🚫 Ce parrain est déjà inscrit avec ce numéro.")
                else:
                    cursor.execute("""
                        INSERT INTO parains (numero_tel, nom, prenom, departement, mot_de_passe)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (numero_tel, nom, prenom, departement, mot_de_passe))
                    conn.commit()
                    st.success("🎉 Parrain inscrit avec succès !")

            elif role == "Filleul":
                cursor.execute("SELECT * FROM filleuls WHERE numero_tel = %s", (numero_tel,))
                if cursor.fetchone():
                    st.error("🚫 Ce filleul est déjà inscrit avec ce numéro.")
                else:
                    cursor.execute("""
                        INSERT INTO filleuls (numero_tel, nom, prenom, departement, mot_de_passe)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (numero_tel, nom, prenom, departement, mot_de_passe))
                    conn.commit()
                    st.success("🎉 Filleul inscrit avec succès !")

        except Exception as e:
            st.error(f"❌ Erreur lors de l'inscription : {e}")
        finally:
            cursor.close()
            conn.close()
