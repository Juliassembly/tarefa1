from flask import flask
import randow

app= Flask(_name_)

piadas = ["Porque é que os polícias não gostam de sabão? Porque  eles preferem deter-gente.",
            "Como se chama o rei dos queijos? Reiqueijão!",]

@app.route("/")
def index():
    return "Hello World!"

@app.route("/piada")
def piada():
    return randow.choice(piadas)

@app.route("/piada/<int:id>")
def piada_id(id):
    if id < 1 or id > len (piadas):
        return "Piada não encontrada" , 404
    return piadas [id - 1]


app.run(host="0.0.0.0", port=8080)
        

        


    
    
