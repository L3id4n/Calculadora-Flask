from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def inicio():
    
    number1 = 0
    number2 = 0
    result = None
    operacao = ""
    mensagem = ""
    mensagem_resultado = ""
    
    if request.method == "POST":
        operacao = request.form["operacao"]
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        
        if operacao == "soma":
            result = float(number1) + float(number2)
            mensagem_resultado = f"O resultado da soma é {result}"
        elif operacao == "subtracao":
            result = float(number1) - float(number2)
            mensagem_resultado = f"O resultado da subtração é {result}"
        elif operacao == "multiplicacao":
            result = float(number1) * float(number2)
            mensagem_resultado = f"O resultado da multiplicação é {result}"
        elif operacao == "divisao":
            if float(number2) == 0:
                mensagem = "Não é possível dividir por zero."
                mensagem_resultado = ""
            else:
                result = float(number1) / float(number2)
                mensagem_resultado = f"O resultado da divisão é {result}"
        elif operacao == "potencia":
            result = float(number1) ** float(number2)
            mensagem_resultado = f"O resultado da potenciação é {result}"
            
        number1 = ""
        number2 = ""
    
    return render_template(
        "index.html",
        number1=number1,
        number2=number2,
        result=result,
        mensagem=mensagem,
        mensagem_resultado=mensagem_resultado,
        operacao=operacao
    )
    
app.run(debug=True)