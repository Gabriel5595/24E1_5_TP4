import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def query_full(table_name):
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + table_name)
        
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results

def main():
    print(query_full("CARGOS"))

main()
