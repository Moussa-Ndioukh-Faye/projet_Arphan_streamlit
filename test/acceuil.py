import inscription
import  streamlit as st


def main():
     st.sidebar.title("Navigation")
     selected_model = st.sidebar.radio("Choisir un modèle", ["inscription", "connexion"])

     if selected_model == "inscription":
         inscription()
     elif selected_model == "connexion":
        connexion()

def connexion():
    print("Connexion réussie.")
