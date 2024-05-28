import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_tables_CARGOS():
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CARGOS(
            CARGO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRICAO VARCHAR(255) NOT NULL,
            SALARIO_BASE DECIMAL(10, 2) NOT NULL,
            NIVEL_CARGO VARCHAR(20) NOT NULL,
            IMPORTANCIA VARCHAR(10) NOT NULL
        )
    """)
        
        connection.commit()
        cursor.close()
    
    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_tables_CARGOS()

main()