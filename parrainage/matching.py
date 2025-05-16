import streamlit as st
from db import get_connection

def correspondance():
    st.header("Matching automatique")

    if st.button("Lancer le matching"):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Obtenir les parrains NON appariés
            cursor.execute("""
                SELECT numero_tel FROM parains
                WHERE numero_tel NOT IN (
                    SELECT parrain_tel FROM correspondances
                )
            """)
            parrains_dispo = [p[0] for p in cursor.fetchall()]

            # Obtenir les filleuls NON appariés
            cursor.execute("""
                SELECT numero_tel FROM filleuls
                WHERE numero_tel NOT IN (
                    SELECT filleul_tel FROM correspondances
                )
            """)
            filleuls_dispo = [f[0] for f in cursor.fetchall()]

            # Faire les appariements
            matches = list(zip(parrains_dispo, filleuls_dispo))

            if not matches:
                st.info("Aucune nouvelle correspondance à créer.")
            else:
                for parrain_tel, filleul_tel in matches:
                    cursor.execute("""
                        INSERT INTO correspondances (parrain_tel, filleul_tel)
                        VALUES (%s, %s)
                    """, (parrain_tel, filleul_tel))
                conn.commit()
                st.success(f"{len(matches)} correspondance(s) créée(s) !")

        except Exception as e:
            st.error(f"Erreur lors du matching : {e}")
        finally:
            cursor.close()
            conn.close()

    # Affichage des correspondances existantes
    st.subheader("Correspondances existantes")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.nom, p.prenom, p.numero_tel, f.nom, f.prenom, f.numero_tel
            FROM correspondances c
            JOIN parains p ON c.parrain_tel = p.numero_tel
            JOIN filleuls f ON c.filleul_tel = f.numero_tel
        """)
        rows = cursor.fetchall()

        if rows:
            for r in rows:
                st.write(f"👨‍🏫 {r[0]} {r[1]} ({r[2]}) ↔ 🧑‍🎓 {r[3]} {r[4]} ({r[5]})")
        else:
            st.info("Aucune correspondance enregistrée.")

    except Exception as e:
        st.error(f"Erreur lors de l'affichage : {e}")
    finally:
        cursor.close()
        conn.close()
