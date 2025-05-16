import streamlit as st
from db import get_connection

import mysql.connector

def inscription():
    st.title("Inscription")
    role = st.selectbox("Je suis :", ["Parrain", "Filleul",])
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    numero = st.text_input("Téléphone")
    departement = st.text_input("Département")
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("S'inscrire"):
        if all([nom, prenom, numero, departement, mdp]):
            try:
                conn = get_connection()
                cursor = conn.cursor()
                table = "parains" if role == "Parrain" else "filleuls"
                cursor.execute(
                    f"INSERT INTO {table} (numero_tel, nom, prenom, departement, mot_de_passe) VALUES (%s, %s, %s, %s, %s)",
                    (int(numero), nom, prenom, departement, mdp)
                )
                conn.commit()
                st.success(f"{role} inscrit avec succès !")
                cursor.close()
                conn.close()
            except mysql.connector.IntegrityError:
                st.error("Ce numéro existe déjà.")
            except Exception as e:
                st.error(f"Erreur : {e}")
        else:
            st.warning("Tous les champs sont obligatoires.")

def connexion():
    st.title("Connexion")
    role = st.radio("Je suis :", ["Parrain", "Filleul"])
    numero = st.text_input("Téléphone")
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if numero and mot_de_passe:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                table = "parains" if role == "Parrain" else "filleuls"
                cursor.execute(
                    f"SELECT * FROM {table} WHERE numero_tel=%s AND mot_de_passe=%s",
                    (numero, mot_de_passe)
                )
                user = cursor.fetchone()
                cursor.close()
                conn.close()

                if user:
                    st.success(f"Bienvenue {user[2]} {user[1]} !")
                    st.session_state.user = {
                        "numero": user[0],
                        "nom": user[1],
                        "prenom": user[2],
                        "role": role
                    }
                else:
                    st.error("Identifiants incorrects.")
            except Exception as e:
                st.error(f"Erreur : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")

def main():
    st.sidebar.title("Navigation")
    selected_model = st.sidebar.radio("Choisir une page", ["inscription", "connexion"])

    if selected_model == "inscription":
        inscription()
    elif selected_model == "connexion":
        connexion()

if __name__ == "__main__":
    main()
