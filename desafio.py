"""desafio.ipynb
"""

from json import dumps
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn


"""Criando o app"""

app = FastAPI()

"""Criando a planilha em json"""

dados = [
    {
    "number" : "1",
    "name" : "Mahesh",
    "age" : 25,
    "city" : "Bangalore",
    "country": "India",
    },
    {
    "number" : "2",
    "name" : "Alex",
    "age" : 26,
    "city" : "Londom",
    "country": "UK",
    },
    {
    "number" : "3",
    "name" : "Daavid",
    "age" : 27,
    "city" : "San Francisco",
    "country": "USA",
    },
    {
    "number" : "4",
    "name" : "John",
    "age" : 28,
    "city" : "Toronto",
    "country": "Cananda",
    },
    {
    "number" : "5",
    "name" : "Chris",
    "age" : 29,
    "city" : "Paris",
    "country": "France",
    }
]

json_string = [dumps(dado) for dado in dados]

"""Rotas"""

@app.get('/index')

async def home():
  """
    Função responsável por retornar uma lista de objetos Json

    return: list(Json): Lista de objetos Json
  """
  return json_string

"""Selecionando a porta"""

ngrok_tunnel = ngrok.connect(8000)

"""Informando a url publica"""

print(f"Public URL: {ngrok_tunnel.public_url}")

"""Ativando o nest_asyncio"""

nest_asyncio.apply()

"""Rodando a aplicação"""

uvicorn.run(app, port=8000)
