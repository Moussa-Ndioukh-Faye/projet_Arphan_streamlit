import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Mets ton mot de passe ici si tu en as mis un dans XAMPP
        database="parainnage"
    )
