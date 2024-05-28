import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_HISTORICO_SALARIOS():
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS HISTORICO_SALARIOS(
            SALARIOS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FUNCIONARIO_ID INTEGER NOT NULL,
            SALARIO DECIMAL(10, 2) NOT NULL,
            MES VARCHAR(20) NOT NULL,
            ANO INTEGER NOT NULL,
            FOREIGN KEY (FUNCIONARIO_ID) REFERENCES FUNCIONARIOS (FUNCIONARIO_ID)
        )
    """)
        
        connection.commit()
        cursor.close()
    
    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_table_HISTORICO_SALARIOS()

main()