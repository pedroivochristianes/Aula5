comando = input("Digitie o seu comando")

match comando:
    case "oi" | "Oi" | "OI":
        print("o seu comando foi oi")
    case "tchau":
        print("o seu comando foi tchau")
    case "Como vai":
        print("o seu comando foi como vai")
    case _: 
        print("Comando invalido")