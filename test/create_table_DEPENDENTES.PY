import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_DEPENDENTES():
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS DEPENDENTES (
            DEPENDENTES_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DEPENDENTE_1 VARCHAR(50),
            SEXO_DEPENDENTE_1 VARCHAR(50),
            IDADE_DEPENDENTE_1 INTEGER,
            PARENTESCO_DEPENDENTE_1 VARCHAR(50),
            DEPENDENTE_2 VARCHAR(50),
            SEXO_DEPENDENTE_2 VARCHAR(50),
            IDADE_DEPENDENTE_2 INTEGER,
            PARENTESCO_DEPENDENTE_2 VARCHAR(50)
            )
    """)
        
        connection.commit()
        cursor.close()
    
    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_table_DEPENDENTES()

main()