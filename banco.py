import sqlite3 as sql

banco = sql.connect("Banco_JICS.db")

cursor = banco.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Alunos(
    nome TEXT NOT NULL,
    turma TEXT NOT NULL,
    matricula PRIMARY KEY INT NOT NULL,
    senha TEXT NOT NULL
)
""")