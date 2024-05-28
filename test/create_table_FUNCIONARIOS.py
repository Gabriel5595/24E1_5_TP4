import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_FUNCIONARIOS():
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS FUNCIONARIOS (
            FUNCIONARIO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FUNCIONARIO_NOME VARCHAR(50) NOT NULL,
            PROJETO_ID INTEGER,
            CARGO_ID INTEGER,
            DEPARTAMENTO_ID INTEGER,
            DEPENDENTES_ID INTEGER,
            SALARIO_REAL DECIMAL(10, 2) NOT NULL,
            TIPO_CONTRATO VARCHAR(3) NOT NULL,
            FOREIGN KEY (PROJETO_ID) REFERENCES PROJETO_ID (PROJETO_ID),
            FOREIGN KEY (CARGO_ID) REFERENCES CARGOS (CARGO_ID),
            FOREIGN KEY (DEPARTAMENTO_ID) REFERENCES DEPARTAMENTOS (DEPARTAMENTO_ID),
            FOREIGN KEY (DEPENDENTES_ID) REFERENCES DEPENDENTES (DEPENDENTES_ID)
            )
    """)
        
        connection.commit()
        cursor.close()
    
    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_table_FUNCIONARIOS()

main()