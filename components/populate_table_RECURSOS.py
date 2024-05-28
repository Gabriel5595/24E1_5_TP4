import sqlite3

from components.read_csv_file import read_csv_file
from components.create_table_RECURSOS import create_table_RECURSOS

def populate_table_RECURSOS():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/recursos.csv"
    file_information = read_csv_file(file_name)
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
        
        cursor.executemany("""
INSERT INTO RECURSOS (PROJETO_ID,
                        RECURSO_DESCRICAO,
                        RECURSO_TIPO,
                        RECURSO_QUANT,
                        DATA_UTILIZACAO) VALUES
                        
                        (:PROJETO_ID,
                        :RECURSO_DESCRICAO,
                        :RECURSO_TIPO,
                        :RECURSO_QUANT,
                        :DATA_UTILIZACAO)""",
[
    {"PROJETO_ID": recurso["PROJETO_ID"],
    "RECURSO_DESCRICAO": recurso["RECURSO_DESCRICAO"],
    "RECURSO_TIPO": recurso["RECURSO_TIPO"],
    "RECURSO_QUANT": recurso["RECURSO_QUANT"],
    "DATA_UTILIZACAO": recurso["DATA_UTILIZACAO"]}
    for recurso in file_information
])
        connection.commit()
        cursor.close()
        
    print('')
    print('Values inserted successfully!')
    print('')