import sqlite3

def drop_tables():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        DROP TABLE IF EXISTS FUNCIONARIOS;
""")
    
    cursor.execute("""
        DROP TABLE IF EXISTS CARGOS;
""")
    
    cursor.execute("""
        DROP TABLE IF EXISTS DEPARTAMENTOS;
""")
    
    cursor.execute("""
        DROP TABLE IF EXISTS DEPENDENTES;
""")
    
    cursor.execute("""
        DROP TABLE IF EXISTS HISTORICO_SALARIOS;
""")
    
    connection.commit()
    
    print('')
    print("Tables dropped sucessfully!")
    print('')
