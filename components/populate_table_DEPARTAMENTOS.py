import sqlite3

from components.read_csv_file import read_csv_file

def populate_table_DEPARTAMENTOS():
    
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/departamentos.csv"
    file_information = read_csv_file(file_name)
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()

        cursor.executemany("""
INSERT INTO DEPARTAMENTOS (NOME_DEPARTAMENTO,
                            FUNCIONARIO_GEN_ID,
                            ANDAR,
                            LOCAL_DEPARTAMENTO) VALUES
                            
                            (:NOME_DEPARTAMENTO,
                            :FUNCIONARIO_GEN_ID,
                            :ANDAR,
                            :LOCAL_DEPARTAMENTO)""",
[
    {"NOME_DEPARTAMENTO": cargo["NOME_DEPARTAMENTO"],
    "FUNCIONARIO_GEN_ID": cargo["FUNCIONARIO_GEN_ID"],
    "ANDAR": cargo["ANDAR"],
    "LOCAL_DEPARTAMENTO": cargo["LOCAL_DEPARTAMENTO"]}
    for cargo in file_information
])
    
        connection.commit()
        cursor.close()
    
    print('')
    print('Values inserted successfully!')
    print('')