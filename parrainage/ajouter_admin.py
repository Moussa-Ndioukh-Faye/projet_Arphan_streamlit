import bcrypt
from db import get_connection

def ajouter_admin(numero_tel, mot_de_passe):
    hashed_pwd = bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO admins (numero_tel, mot_de_passe) VALUES (%s, %s)", (numero_tel, hashed_pwd))
        conn.commit()
        print(f"Admin {numero_tel} ajouté avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'admin : {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    numero = input("Numéro de téléphone admin (9 chiffres) : ")
    mdp = input("Mot de passe admin : ")
    ajouter_admin(numero, mdp)
