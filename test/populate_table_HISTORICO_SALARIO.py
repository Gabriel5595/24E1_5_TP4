import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file
from components.create_table_HISTORICO_SALARIOS import create_table_HISTORICO_SALARIOS

def populate_table_HISTORICO_SALARIOS(file_information):
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
        
        cursor.executemany("""
INSERT INTO HISTORICO_SALARIOS (FUNCIONARIO_ID,
                            SALARIO,
                            MES,
                            ANO) VALUES
                            
                            (:FUNCIONARIO_ID,
                            :SALARIO,
                            :MES,
                            :ANO)""",
[
    {"FUNCIONARIO_ID": historico_salario["FUNCIONARIO_ID"],
    "SALARIO": historico_salario["SALARIO"],
    "MES": historico_salario["MES"],
    "ANO": historico_salario["ANO"]}
    for historico_salario in file_information
])
    
        connection.commit()
        cursor.close()
        
    print('')
    print('Values inserted successfully!')
    print('')
    
def main():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/historico_salarios.csv"
    file_information = read_csv_file(file_name)
    
    print("***FILE INFORMATION***")
    print(file_information)
    print("**********************")
    
    create_table_HISTORICO_SALARIOS()
    
    populate_table_HISTORICO_SALARIOS(file_information)

main()