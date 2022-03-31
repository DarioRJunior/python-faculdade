salario = float(input("Digite o seu salário: "))
aumentoSalario = int(input("Digite a porcentagem de aumento: "))
aumentoCalculo = aumentoSalario * salario
aumentoTotal = aumentoCalculo / 100
print(f"O aumento será de R$ {aumentoTotal}")
salarioAtual = aumentoTotal + salario
print(f"Seu salário atual é de R$ {salarioAtual}")