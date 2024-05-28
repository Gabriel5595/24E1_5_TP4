import sqlite3

def create_table_HISTORICO_SALARIOS():
    connection = sqlite3.connect("database.db")
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
    
    print('')
    print("Table created sucessfully!")
    print('')