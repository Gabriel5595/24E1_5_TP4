import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file
from components.create_table_PROJETOS import create_table_PROJETOS

def populate_table_PROJETOS(file_information):
    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()
        
        cursor.executemany("""
INSERT INTO PROJETOS (FUNC_RESPONSAVEL,
                        PROJETO_NOME,
                        PROJETO_DESCRICAO,
                        DATA_INICIO,
                        DATA_FINAL,
                        CUSTO_PROJETO,
                        STATUS) VALUES
                        
                        (:FUNC_RESPONSAVEL,
                        :PROJETO_NOME,
                        :PROJETO_DESCRICAO,
                        :DATA_INICIO,
                        :DATA_FINAL,
                        :CUSTO_PROJETO,
                        :STATUS)""",
[
    {"FUNC_RESPONSAVEL": projeto["FUNC_RESPONSAVEL"],
    "PROJETO_NOME": projeto["PROJETO_NOME"],
    "PROJETO_DESCRICAO": projeto["PROJETO_DESCRICAO"],
    "DATA_INICIO": projeto["DATA_INICIO"],
    "DATA_FINAL": projeto["DATA_FINAL"],
    "CUSTO_PROJETO": projeto["CUSTO_PROJETO"],
    "STATUS": projeto["STATUS"]}
    for projeto in file_information
])
        
        connection.commit()
        cursor.close()
        
    print('')
    print('Values inserted successfully!')
    print('')

def main():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/projetos.csv"
    file_information = read_csv_file(file_name)
    
    print("***FILE INFORMATION***")
    print(file_information)
    print("**********************")
    
    create_table_PROJETOS()
    
    populate_table_PROJETOS(file_information)

main()