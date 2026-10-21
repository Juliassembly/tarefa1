import random
from flask import Flask
from flask_cors import CORS  

# Correção: O correto é usar dois underscores a__name__ntes e depois ()
app = Flask(__name__)
CORS(app)

pokemons = [
    {
        "id": 1,
        "nome": "Squirtle",
        "tipo": "Água"
    
    },
        {
        "id": 2,
        "nome": "Bulbasaur",
        "tipo": "Planta e Veneno "
    },
]



@app.route("/")
def index():
    return "Hello World!"


@app.route("/pokémon")
def pokémon():
    return random.choice(pokemons)


@app.route("/pokémon/<int:id>", methods=["GET"])
def pokémon_id(id):
    # Validação do ID fornecido na rota
    if id < 1 or id > len(pokemons):
        return "pokémon não encontrada", 404
    return pokémon[id - 1]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083) 





