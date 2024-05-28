from typing import Union
from fastapi import FastAPI

from components.drop_table import drop_tables
from components.query_full import query_full
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
from components.query_1 import query_1
from components.query_2 import query_2
from components.query_3 import query_3
from components.query_4 import query_4
from components.query_5 import query_5

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

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    @app.get("/query_1")
    async def get_query_1():
        return query_1()

    @app.get("/query_2")
    async def get_query_2():
        return query_2()

    @app.get("/query_3")
    async def get_query_3():
        return query_3()

    @app.get("/query_4")
    async def get_query_4():
        return query_4()

    @app.get("/query_5")
    async def get_query_5():
        return query_5()

    @app.get("/cargos")
    async def get_cargos():
        return query_full("cargos")

    @app.get("/departamentos")
    async def get_departamentos():
        return query_full("departamentos")

    @app.get("/dependetes")
    async def get_dependentes():
        return query_full("dependetes")

    @app.get("/funcionarios")
    async def get_funcionarios():
        return query_full("funcionarios")

    @app.get("/historico_salarios")
    async def get_historico_salarios():
        return query_full("historico_salarios")

    @app.get("/projetos")
    async def get_projetos():
        return query_full("projetos")

    @app.get("/recursos")
    async def get_recursos():
        return query_full("recursos")
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)

main()