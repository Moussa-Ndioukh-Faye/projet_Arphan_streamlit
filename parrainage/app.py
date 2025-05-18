import streamlit as st
from inscription import inscription
from connexion import connexion
from admin import admin
from liste import afficher_listes
from matching import correspondance

def main():
    st.set_page_config(
        page_title="ESP - Site de Parrainage",
        page_icon="🤝",
        layout="centered"
    )

    # Initialisation des variables de session
    if 'connecte' not in st.session_state:
        st.session_state.connecte = False
    if 'role' not in st.session_state:
        st.session_state.role = None
    if 'navigation' not in st.session_state:
        st.session_state.navigation = "🏠 Accueil"

    # ░░░░░░░░░░░░░░░░░░░░░
    # 🌐 Menu latéral
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXaZ_VUG6yGJZX_0nEnIwOFOigvvnM9IGfng&s",
        width=150
    )
    st.sidebar.title("📚 Menu de navigation")

    if st.session_state.connecte:
        options = ["🏠 Accueil", "🤖 Matching", "📋 Listes"]
        if st.session_state.role == "admin":
            options.append("🔒 Admin")
        options.append("🚪 Déconnexion")
    else:
        options = ["🏠 Accueil", "📝 Inscription", "🔐 Connexion"]

    selection = st.sidebar.selectbox("Sélectionner une page :", options)
    st.session_state.navigation = selection

    # ░░░░░░░░░░░░░░░░░░░░░
    # 🧭 Routage des pages
    if st.session_state.navigation == "🏠 Accueil":
        st.title("🤝 Bienvenue sur le site de parrainage de l'ESP")
        st.markdown("---")
        st.markdown("""
        <div style='text-align: justify;'>
        <h4>🎯 Objectif :</h4>
        Ce site met en relation les <b>parrains</b> (étudiants expérimentés) avec les <b>filleuls</b> (nouveaux à l'ESP).
        <ul>
            <li>👨‍🏫 Les parrains partagent leur expérience</li>
            <li>🧑‍🎓 Les filleuls sont mieux accompagnés</li>
            <li>🔄 Matching automatique et équitable</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("___")
        st.subheader("🚀 Que souhaitez-vous faire ?")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 📝 S'inscrire")
            st.button("Accéder", key="btn_inscription", on_click=lambda: st.session_state.update({'navigation': "📝 Inscription"}))

        with col2:
            st.markdown("### 🔐 Se connecter")
            st.button("Accéder", key="btn_connexion", on_click=lambda: st.session_state.update({'navigation': "🔐 Connexion"}))

        with col3:
            st.markdown("### 🤖 Matching")
            st.button("Accéder", key="btn_matching", disabled=not st.session_state.connecte)

    elif st.session_state.navigation == "📝 Inscription":
        inscription()

    elif st.session_state.navigation == "🔐 Connexion":
        connexion()

    elif st.session_state.navigation == "🤖 Matching":
        correspondance()

    elif st.session_state.navigation == "📋 Listes":
        afficher_listes()

    elif st.session_state.navigation == "🔒 Admin":
        admin()

    elif st.session_state.navigation == "🚪 Déconnexion":
        st.session_state.connecte = False
        st.session_state.role = None
        st.success("✅ Vous avez été déconnecté.")

        # ✅ Version compatible avec toutes les versions
        try:
            st.rerun()  # Pour les versions >= 1.18
        except AttributeError:
            st.experimental_rerun()  # Pour les versions plus anciennes

if __name__ == "__main__":
    main()
