import random
from flask import Flask

# Correção: O correto é usar dois underscores antes e depois (__name__)
app = Flask(__name__)

# Correção: As piadas dentro da lista precisam de estar entre aspas
piadas = [
    "Porque é que os polícias não gostam de sabão? Porque eles preferem deter-gente.",
    "Como se chama o rei dos queijos? Reiqueijão!",
]


@app.route("/")
def index():
    return "Hello World!"


@app.route("/piada")
def piada():
    return random.choice(piadas)


@app.route("/piada/<int:id>", methods=["GET"])
def piada_id(id):
    # Validação do ID fornecido na rota
    if id < 1 or id > len(piadas):
        return "Piada não encontrada", 404
    return piadas[id - 1]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083) 
