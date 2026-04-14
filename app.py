from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)
app.json.ensure_ascii = False

respostas = [
    "Sim, com certeza!",
    "Sem dúvida.", 
    "Definitivamente sim!",
    "Pode contar com isso!",
    "Na minha opinião, sim.",
    "Provavelmente.",
    "Boa ideia!",
    "Sim.",
    "Os sinais apontam que sim.",
    "Claramente é sim.",
    "Fiquei confuso, tente novamente.", 
    "Pergunte novamente mais tarde.",
    "Melhor não te contar agora.",
    "Não é possível prever agora.",
    "Concentre-se e pergunte novamente.",
    "Acho que não.",
    "Minha resposta é não.",
    "Minhas fontes dizem que não.",
    "Claramente que não.",
    "Duvido muito."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shake")
def sorteia():
    resposta = random.choice(respostas)
    return jsonify({"resposta" : resposta})

if __name__ == "__main__":
    app.run(debug=True)