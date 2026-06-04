from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def inicio():
    
    number1 = 0
    number2 = 0
    result = 0
    operacao = ""
    
    if request.method == "POST":
        operacao = request.form["operacao"]
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        if operacao == "soma":
            result = float(number1) + float(number2)
        elif operacao == "subtracao":
            result = float(number1) - float(number2)
        elif operacao == "multiplicacao":
            result = float(number1) * float(number2)
        elif operacao == "divisao":
            result = float(number1) / float(number2)
    
    return render_template(
        "index.html",
        number1=number1,
        number2=number2,
        result=result,
        operacao=operacao
    )
    
app.run(debug=True)