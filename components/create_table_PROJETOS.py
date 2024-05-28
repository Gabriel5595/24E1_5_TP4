import sqlite3

def create_table_PROJETOS():
    connection = sqlite3.connect("database.db")
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

    print('')
    print("Table created sucessfully!")
    print('')