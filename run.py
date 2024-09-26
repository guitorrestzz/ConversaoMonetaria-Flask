from flask import Flask, render_template, redirect, request
import requests  # Importação correta de requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        moeda_real = request.form.get("real")
        moeda_dolar = request.form.get("dolar")
        cotacao = request.form.get("cotacao")

        requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao_api = requisicao.json()

        moeda_real = float(moeda_real) if moeda_real else 0
        moeda_dolar = float(moeda_dolar) if moeda_dolar else 0
        cotacao = float(cotacao) if cotacao else float(cotacao_api['USD']['bid'])

        if moeda_real == 0:
            moeda_real = moeda_dolar * cotacao
        elif moeda_dolar == 0:
            moeda_dolar = moeda_real / cotacao

        return render_template("index.html", moeda_real=str(moeda_real),
                                moeda_dolar=str(moeda_dolar), 
                                cotacao=str(cotacao))
    else:
        return render_template("index.html")

@app.route("/teste")
def teste():
    return render_template("teste.html")

if __name__ == '__main__':
    app.run("127.0.0.1", port=80, debug=True)
