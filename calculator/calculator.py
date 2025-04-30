def calculo(x:int, op:str, y:int) -> float: 

    if op == "+":
        resultado = x + y
        return resultado
    elif op == "-":
        resultado = x - y
        return resultado
    elif op == "*":
        resultado = x * y
        return resultado
    elif op == "/":
        resultado = x / y
        return resultado
    elif op == "**":
        resultado = x ** y
        return resultado
    else:
        print("Escolha um operador válido:")
        return None

def calculator():

    x = int(input("Digite um valor: "))
    op = input("Qual o Operador (+, -, *, /, **): ").strip().upper()
    y = int(input("Qual o segundo valor: "))
            
    resultado = calculo(x, op, y)
    if resultado is not None:
        print(f"Resultado: {resultado}")

    while True:
        continua = input("Deseja continuar? (S/N): ").strip().upper()
        if continua == "N":
            print("Calculadora encerrada.")
            break
        elif continua == "S":
            op = input("Qual o Operador (+, -, *, /, **): ")
            y = int(input("Qual o valor: "))
            resultado = calculo(resultado, op, y)
            if resultado is not None:
                print(f"Resultado: {resultado}")
            else:
                print("Operação inválida. Recomece a operação.")
                break
        else:
            print("Entrada inválida. Responda apenas com S ou N.")
           

calculator()