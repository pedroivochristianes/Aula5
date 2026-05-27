print ("1 - cadastrar | 2 - listar | 3 - sair")

opcao = int(input(""))

match opcao: 
    case 1: 
        print("Você esclheu CADASTRAR.")
    case 2:
        print("Você escolheu LISTAR")
    case 3: 
        print("Você escolheu SAIR")
    case _: 
        print("Comando invalido") 
