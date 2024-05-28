import sqlite3

def create_table_DEPENDENTES():
    connection = sqlite3.connect("database.db")
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
    
    print('')
    print("Table created sucessfully!")
    print('')