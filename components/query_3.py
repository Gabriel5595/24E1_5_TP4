import sqlite3

def query_3():
    print()
    print("*** QUERY 3 ***")
    print("Calcular o custo total dos projetos por departamento, considerando apenas os projetos 'Concluídos'.")
    print()
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT
                            DEPARTAMENTOS.NOME_DEPARTAMENTO,
                            SUM(PROJETOS.CUSTO_PROJETO) AS CUSTO_TOTAL_PROJETOS
                        FROM PROJETOS
                        JOIN FUNCIONARIOS ON PROJETOS.FUNC_RESPONSAVEL = FUNCIONARIOS.FUNCIONARIO_ID
                        JOIN DEPARTAMENTOS ON FUNCIONARIOS.DEPARTAMENTO_ID = DEPARTAMENTOS.DEPARTAMENTO_ID
                        WHERE PROJETOS.STATUS = 'Concluído'
                        GROUP BY DEPARTAMENTOS.NOME_DEPARTAMENTO;
                        """)
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results