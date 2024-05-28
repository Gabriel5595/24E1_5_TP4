import sqlite3

from components.read_csv_file import read_csv_file

def populate_table_CARGOS():
    
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/cargos.csv"
    file_information = read_csv_file(file_name)
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
        
        cursor.executemany("""
    INSERT INTO CARGOS (DESCRICAO,
                        SALARIO_BASE,
                        NIVEL_CARGO,
                        IMPORTANCIA) VALUES
                        
                        (:DESCRICAO,
                        :SALARIO_BASE,
                        :NIVEL_CARGO,
                        :IMPORTANCIA)""",
    [
        {"DESCRICAO": cargo["DESCRICAO"],
        "SALARIO_BASE": cargo["SALARIO_BASE"],
        "NIVEL_CARGO": cargo["NIVEL_CARGO"],
        "IMPORTANCIA": cargo["IMPORTANCIA"]}
        for cargo in file_information
    ])
        
        connection.commit()
        cursor.close()
    
    print('')
    print('Values inserted successfully!')
    print('')