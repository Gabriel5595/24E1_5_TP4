import sqlite3

def query_2():
    print()
    print("*** QUERY 2 ***")
    print("Identificar os três recursos materiais mais usados nos projetos, listando a descrição do recurso e a quantidade total usada.")
    print()
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT
                        RECURSO_DESCRICAO,
                        RECURSO_TIPO,
                        SUM(RECURSO_QUANT) AS TOTAL_QUANTIDADE
                    FROM RECURSOS
                    GROUP BY RECURSO_DESCRICAO
                    ORDER BY TOTAL_QUANTIDADE DESC
                    LIMIT 3;
                    """)
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results