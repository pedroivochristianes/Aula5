nota = float(input("Digite a nota do aluno:"))

match nota:
    case nota if nota >= 9.5: 
        print("Nossa que nota excelente.")
    case nota if nota > 5 and nota <=9.5:
        print("Aluno aprovado.")
    case nota if nota <=5:
        print("Nota abaixo da média.")
    case nota if nota <=3:
        print("Aluno reprovado.") 
