import sqlite3

def query_4():
    print()
    print("*** QUERY 4 ***")
    print(" Listar todos os projetos com seus respectivos nomes, custo, data de início, data de conclusão e o nome do funcionário responsável, que estejam 'Em Execução'")
    print()
    
    with sqlite3.connect("database.db", timeout=60) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT DISTINCT
                            PROJETOS.PROJETO_NOME,
                            PROJETOS.CUSTO_PROJETO,
                            PROJETOS.DATA_INICIO,
                            CASE
                                WHEN PROJETOS.DATA_FINAL = "NULL" THEN 'Não definido'
                                ELSE PROJETOS.DATA_FINAL
                            END AS DATA_FINAL,
                            FUNCIONARIOS.FUNCIONARIO_NOME AS RESPONSAVEL
                        FROM PROJETOS
                        JOIN FUNCIONARIOS ON PROJETOS.FUNC_RESPONSAVEL = FUNCIONARIOS.FUNCIONARIO_ID
                        WHERE PROJETOS.STATUS = 'Em Execução';
                        """)
        results = [dict(row) for row in cursor.fetchall()]
        for line in results:
            print(line)
        
        return results