import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_RECURSOS():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RECURSOS (
        RECURSO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PROJETO_ID INTEGER NOT NULL,
        RECURSO_DESCRICAO VARCHAR(255) NOT NULL,
        RECURSO_TIPO VARCHAR(255) NOT NULL,
        RECURSO_QUANT INT NOT NULL,
        DATA_UTILIZACAO VARCHAR(10),
        FOREIGN KEY (PROJETO_ID) REFERENCES PROJETOS (PROJETO_ID)
        )
""")

    print('')
    print("Table created sucessfully!")
    print('')