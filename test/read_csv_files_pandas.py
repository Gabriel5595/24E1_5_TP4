import csv
import pandas
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def read_csv_files_pandas(file_name):
    file_information = pandas.read_csv(file_name)
    
    print('')
    print("Reading sucessfull!")
    print('')
    
    return file_information

def main():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/cargos.csv"
    file_information = read_csv_files_pandas(file_name)
    
    print(file_information)

main()