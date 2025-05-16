import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # mets ton mot de passe MySQL ici si tu en as défini un
        database="parainnage"
    )
