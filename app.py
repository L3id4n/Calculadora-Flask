from flask import Flask, request, render_template

app = Flask(__name__)

historico = []

@app.route("/", methods=["GET", "POST"])
def inicio():
    
    global historico
    
    number1 = ""
    number2 = ""
    result = None
    operacao = ""
    mensagem_resultado = ""
    
    if request.method == "POST":
        
        action = request.form["action"]
        
        if action == "limpar":
            historico = []
        
        else:
            operacao = request.form["operacao"]
            number1 = float(request.form["number1"])
            number2 = float(request.form["number2"])
            
        if operacao == "soma":
            result = float(number1) + float(number2)
            mensagem_resultado = f"O resultado da soma é {result}"
            historico.append(f"{number1} + {number2} = {result}")
        elif operacao == "subtracao":
            result = float(number1) - float(number2)
            mensagem_resultado = f"O resultado da subtração é {result}"
            historico.append(f"{number1} - {number2} = {result}")
        elif operacao == "multiplicacao":
            result = float(number1) * float(number2)
            mensagem_resultado = f"O resultado da multiplicação é {result}"
            historico.append(f"{number1} * {number2} = {result}")
        elif operacao == "divisao":
            if float(number2) == 0:
                result = "indefinido"
                mensagem_resultado = f"Não é possível dividir por 0. Resultado {result}"
                historico.append(f"{number1} / {number2} = {result}")
            else:
                result = float(number1) / float(number2)
                mensagem_resultado = f"O resultado da divisão é {result}"
                historico.append(f"{number1} / {number2} = {result}")
        elif operacao == "potencia":
            if float(number1) == 0 and float(number2) == 0:
                result = "indefinido"
                mensagem_resultado = f"Não é possivel elevar o 0 por 0!"
                historico.append(f"{number1} ^ {number2} = {result}")
            else:
                result = float(number1) ** float(number2)
                mensagem_resultado = f"O resultado da potência é {result}"
                historico.append(f"{number1} ^ {number2} = {result}")

    number1 = ""
    number2 = ""
        
    
    return render_template(
        "index.html",
        number1=number1,
        number2=number2,
        result=result,
        operacao=operacao,
        mensagem_resultado=mensagem_resultado,
        historico=historico,
    )

app.run(debug=True)