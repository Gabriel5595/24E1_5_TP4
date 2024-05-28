import csv
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def read_csv_file(file_name):
    with open(file_name, mode="r", newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [line for line in csv_reader]
    return data

def main():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP4/resources/cargos.csv"
    file_information = read_csv_file(file_name)
    
    print(file_information)

main()