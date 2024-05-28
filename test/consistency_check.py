import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.drop_table import drop_tables
from components.create_table_CARGOS import create_table_CARGOS
from components.create_table_DEPARTAMENTOS import create_table_DEPARTAMENTOS
from components.create_table_FUNCIONARIOS import create_table_FUNCIONARIOS
from components.create_table_DEPENDENTES import create_table_DEPENDENTES
from components.create_table_HISTORICO_SALARIOS import create_table_HISTORICO_SALARIOS
from components.create_table_PROJETOS import create_table_PROJETOS
from components.create_table_RECURSOS import create_table_RECURSOS
from components.populate_table_CARGO import populate_table_CARGOS
from components.populate_table_DEPARTAMENTOS import populate_table_DEPARTAMENTOS
from components.populate_table_FUNCIONARIOS import populate_table_FUNCIONARIOS
from components.populate_table_DEPARTAMENTOS import populate_table_DEPARTAMENTOS
from components.populate_table_DEPENDENTES import populate_table_DEPENDENTES
from components.populate_table_HISTORICO_SALARIO import populate_table_HISTORICO_SALARIOS
from components.populate_table_RECURSOS import populate_table_RECURSOS
from components.populate_table_PROJETOS import populate_table_PROJETOS

def consistency_check():
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        
        print()
        print("*** TABLE CARGOS ***")
        cursor.execute("SELECT * FROM CARGOS")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE DEPARTAMENTOS ***")
        cursor.execute("SELECT * FROM DEPARTAMENTOS")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE DEPENDENTES ***")
        cursor.execute("SELECT * FROM DEPENDENTES")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE FUNCIONARIOS ***")
        cursor.execute("SELECT * FROM FUNCIONARIOS")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE HISTORICO_SALARIOS ***")
        cursor.execute("SELECT * FROM HISTORICO_SALARIOS")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE PROJETOS ***")
        cursor.execute("SELECT * FROM PROJETOS")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE RECURSOS ***")
        cursor.execute("SELECT * FROM RECURSOS")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** JOIN TEST ***")
        cursor.execute("""SELECT * FROM RECURSOS
                        JOIN PROJETOS ON RECURSOS.PROJETO_ID = PROJETOS.PROJETO_ID""")
        results = cursor.fetchall()
        for line in results:
            print(line)

def main():
    
    drop_tables()
    
    create_table_CARGOS()
    create_table_DEPENDENTES()
    create_table_DEPARTAMENTOS()
    create_table_FUNCIONARIOS()
    create_table_HISTORICO_SALARIOS()
    create_table_PROJETOS()
    create_table_RECURSOS()
    
    populate_table_CARGOS()
    populate_table_DEPARTAMENTOS()
    populate_table_FUNCIONARIOS()
    populate_table_DEPENDENTES()
    populate_table_HISTORICO_SALARIOS()
    populate_table_PROJETOS()
    populate_table_RECURSOS()
    
    consistency_check()

main()