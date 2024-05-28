import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file
from components.create_table_DEPARTAMENTOS import create_table_DEPARTAMENTOS

def populate_table_DEPARTAMENTOS(file_information):
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
    
def main():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/departamentos.csv"
    file_information = read_csv_file(file_name)
    
    print("***FILE INFORMATION***")
    print(file_information)
    print("**********************")
    
    create_table_DEPARTAMENTOS()
    
    populate_table_DEPARTAMENTOS(file_information)

main()