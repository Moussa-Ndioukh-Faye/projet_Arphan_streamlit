import streamlit as st

def header():
    st.markdown(
        """
        <style>
            .navbar {
                background-color: #4CAF50;
                padding: 10px;
                color: white;
                font-weight: bold;
                font-size: 20px;
                text-align: center;
                margin-bottom: 20px;
            }
            .logout-btn {
                float: right;
                background-color: #f44336;
                border: none;
                color: white;
                padding: 5px 10px;
                cursor: pointer;
                font-weight: normal;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="navbar">Site de Parrainage ESP', unsafe_allow_html=True)
    if 'username' in st.session_state:
        st.markdown(f'<div style="float:right">Connecté: {st.session_state.get("username")} ({st.session_state.get("role")})</div>', unsafe_allow_html=True)
        if st.button("Déconnexion"):
            st.session_state.clear()
            st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
