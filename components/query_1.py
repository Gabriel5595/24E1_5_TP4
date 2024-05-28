import sqlite3

def query_1():
    print()
    print("*** QUERY 1 ***")
    print("Trazer a média dos salários (atual) dos funcionários responsáveis por projetos concluídos, agrupados por departamento.")
    print()
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT
                            DEPARTAMENTOS.NOME_DEPARTAMENTO,
                            AVG(FUNCIONARIOS.SALARIO_REAL) AS MEDIA_SALARIOS
                        FROM FUNCIONARIOS
                        JOIN PROJETOS ON FUNCIONARIOS.FUNCIONARIO_ID = PROJETOS.FUNC_RESPONSAVEL
                        JOIN DEPARTAMENTOS ON FUNCIONARIOS.DEPARTAMENTO_ID = DEPARTAMENTOS.DEPARTAMENTO_ID
                        WHERE PROJETOS.STATUS = 'Concluído'
                        GROUP BY DEPARTAMENTOS.NOME_DEPARTAMENTO;
                        """)
        
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results