import streamlit as st
from db import get_connection
import random
import pandas as pd
from datetime import datetime

def correspondance():
    st.subheader("🔁 Appariement aléatoire Parrain ↔ Filleul")

    conn = get_connection()
    cursor = conn.cursor()

    # 🔒 Sécurité : protection admin pour la réinitialisation
    with st.expander("🔐 Réinitialisation des correspondances (admin seulement)"):
        password = st.text_input("Mot de passe admin :", type="password")
        if st.button("🔄 Réinitialiser les correspondances"):
            if password == "admin123":
                cursor.execute("DELETE FROM correspondances")
                conn.commit()
                st.success("✅ Correspondances supprimées avec succès.")
                conn.close()
                st.stop()
            else:
                st.error("❌ Mot de passe incorrect.")

    # 🎯 Lancer le matching
    if st.button("🎯 Lancer le matching aléatoire"):
        # Récupérer les parrains non appariés
        cursor.execute("""
            SELECT numero_tel FROM parains
            WHERE numero_tel NOT IN (SELECT parrain_tel FROM correspondances)
        """)
        parrains = [row[0] for row in cursor.fetchall()]

        # Récupérer les filleuls non appariés
        cursor.execute("""
            SELECT numero_tel FROM filleuls
            WHERE numero_tel NOT IN (SELECT filleul_tel FROM correspondances)
        """)
        filleuls = [row[0] for row in cursor.fetchall()]

        # Mélanger aléatoirement
        random.shuffle(parrains)
        random.shuffle(filleuls)

        # Appariement
        nb_matches = min(len(parrains), len(filleuls))
        matches = list(zip(parrains[:nb_matches], filleuls[:nb_matches]))

        for parrain, filleul in matches:
            cursor.execute("""
                INSERT INTO correspondances (parrain_tel, filleul_tel, date_matching)
                VALUES (%s, %s, %s)
            """, (parrain, filleul, datetime.now()))

        conn.commit()
        st.success(f"🎉 {nb_matches} correspondance(s) effectuée(s).")

    # 📋 Affichage des correspondances
    cursor.execute("""
        SELECT p.nom, p.prenom, f.nom, f.prenom, c.date_matching
        FROM correspondances c
        JOIN parains p ON c.parrain_tel = p.numero_tel
        JOIN filleuls f ON c.filleul_tel = f.numero_tel
    """)
    resultats = cursor.fetchall()
    conn.close()

    if resultats:
        st.markdown("### ✅ Correspondances existantes")
        data = []
        for parrain_nom, parrain_prenom, filleul_nom, filleul_prenom, date_match in resultats:
            data.append({
                "Parrain": f"{parrain_prenom} {parrain_nom}",
                "Filleul": f"{filleul_prenom} {filleul_nom}",
                "Date de Matching": date_match.strftime("%Y-%m-%d %H:%M")
            })
        df = pd.DataFrame(data)
        st.dataframe(df)

        # 📤 Export CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Télécharger les correspondances (CSV)",
            data=csv,
            file_name='correspondances.csv',
            mime='text/csv'
        )
    else:
        st.info("Aucune correspondance encore effectuée.")
