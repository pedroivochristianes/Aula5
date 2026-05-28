
# informar os números 
numero1 = int(input("Digite o primeiro númeoro da operação: "))
numero2 = int(input("Digite o segundo númeoro da operação: "))

# o operador pode ser +, - , *, /
operacao = input("Digite o simbolo para escolher o calculo: \n + soma | - subtração | * multiplicação | / divisão") 

# operação
match operacao:
    case "+":
        print(numero1 + numero2)
    case "-":
        print(numero1 - numero2)
    case "/":
        print(numero1 / numero2)
    case "*":
        print(numero1 * numero2)
    case _:
        print("Operação inválida.")