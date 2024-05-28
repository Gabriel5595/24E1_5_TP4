import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_PROJETOS():
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PROJETOS (
            PROJETO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FUNC_RESPONSAVEL INTEGER NOT NULL,
            PROJETO_NOME VARCHAR(50) NOT NULL,
            PROJETO_DESCRICAO VARCHAR(255) NOT NULL,
            DATA_INICIO VARCHAR(10) NOT NULL,
            DATA_FINAL VARCHAR(10),
            CUSTO_PROJETO DECIMAL(12, 2) NOT NULL,
            STATUS VARCHAR(50) NOT NULL,
            FOREIGN KEY (FUNC_RESPONSAVEL) REFERENCES FUNCIONARIOS (FUNCIONARIO_ID)
            )
    """)
        
        connection.commit()
        cursor.close()

    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_table_PROJETOS()

main()