import sqlite3

def create_table_CARGOS():
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