import sqlite3

def query_full(table_name):
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + table_name)
        
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results
