import sqlite3

def query_5():
    print()
    print("*** QUERY 5 ***")
    print(" Identificar o projeto com o maior número de dependentes envolvidos, considerando que os dependentes são associados aos funcionários que estão gerenciando os projetos.")
    print()
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT
                            PROJETOS.PROJETO_NOME,
                            COUNT(DEPENDENTES.DEPENDENTES_ID) AS NUM_DEPENDENTES
                        FROM PROJETOS
                        INNER JOIN FUNCIONARIOS ON PROJETOS.FUNC_RESPONSAVEL = FUNCIONARIOS.FUNCIONARIO_ID
                        LEFT JOIN DEPENDENTES ON FUNCIONARIOS.DEPENDENTES_ID = DEPENDENTES.DEPENDENTES_ID
                        GROUP BY PROJETOS.PROJETO_NOME
                        ORDER BY COUNT(DEPENDENTES.DEPENDENTES_ID) DESC
                        LIMIT 1;
                        """)
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results