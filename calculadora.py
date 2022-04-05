from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
app.url_map.strict_slashes = False

@app.route('/')
def main():
    return render_template('calculator.html')

@app.route('/calcular', methods=['POST', 'GET'])
def calculate():
    valor1 = request.form["valor1"]
    valor2 = request.form["valor1"]
    operacao = request.form["operacao"]

    if operacao == "soma":
        result = int(valor1) + int(valor2)
        return render_template("calculator.html", result=result)

    elif operacao == "subtracao":
        result = int(valor1) - int(valor2)
        return render_template("calculator.html", result=result)

    elif operacao == "multiplicacao":
        result = int(valor1) * int(valor2)
        return render_template("calculator.html", result=result)

    elif operacao == "divisao":
        result = int(valor1) / int(valor2)
        return render_template("calculator.html", result=result)

    else:
        return render_template("calculator.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("page404.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
