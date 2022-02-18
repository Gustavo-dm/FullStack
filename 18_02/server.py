from flask import Flask, request, render_template
import os


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('calc.html')


@app.route('/calcula', methods=["POST", "GET"])
def calcula():
    val1 = int(request.form["valor1"])
    val2 = int(request.form["valor2"])
    operacao = request.form["operacao"]
    result = 0
    if(operacao == 'soma'):
        result = val1 + val2
    elif(operacao == 'subtracao'):
        result = val1 - val2
    elif(operacao == 'multiplicacao'):
        result = val1 * val2
    elif(operacao == 'divisao'):
        result = val1 / val2
    else:
        result = 'Operacao Invalida'
    return str(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
