import sqlite3

from components.read_csv_file import read_csv_file

def populate_table_DEPENDENTES():
    
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/dependentes.csv"
    file_information = read_csv_file(file_name)
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
        
        cursor.executemany("""
INSERT INTO DEPENDENTES (DEPENDENTE_1,
                        SEXO_DEPENDENTE_1,
                        IDADE_DEPENDENTE_1,
                        PARENTESCO_DEPENDENTE_1,
                        DEPENDENTE_2,
                        SEXO_DEPENDENTE_2,
                        IDADE_DEPENDENTE_2,
                        PARENTESCO_DEPENDENTE_2) VALUES

                        (:DEPENDENTE_1,
                        :SEXO_DEPENDENTE_1,
                        :IDADE_DEPENDENTE_1,
                        :PARENTESCO_DEPENDENTE_1,
                        :DEPENDENTE_2,
                        :SEXO_DEPENDENTE_2,
                        :IDADE_DEPENDENTE_2,
                        :PARENTESCO_DEPENDENTE_2)""",
[
    {"DEPENDENTE_1": dependente["DEPENDENTE_1"],
    "SEXO_DEPENDENTE_1": dependente["SEXO_DEPENDENTE_1"],
    "IDADE_DEPENDENTE_1": dependente["IDADE_DEPENDENTE_1"],
    "PARENTESCO_DEPENDENTE_1": dependente["PARENTESCO_DEPENDENTE_1"],
    "DEPENDENTE_2": dependente["DEPENDENTE_2"],
    "SEXO_DEPENDENTE_2": dependente["SEXO_DEPENDENTE_2"],
    "IDADE_DEPENDENTE_2": dependente["IDADE_DEPENDENTE_2"],
    "PARENTESCO_DEPENDENTE_2": dependente["PARENTESCO_DEPENDENTE_2"]}
    for dependente in file_information
])
        connection.commit()
        cursor.close()
        
    print('')
    print('Values inserted successfully!')
    print('')