nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura*altura)

if imc <= 18.5:
    
    print(f"{nome}, seu IMC é de {round(imc)}, você está abaixo do peso")
    
elif imc >= 18.6 and imc <= 24.9:
    
    print(f"{nome}, seu IMC é de {round(imc)}, seu peso está normal.")
    
elif imc >= 25.0 and imc <= 29.0:
    
    print(f"{nome}, seu IMC é de {round(imc)}, você está com sobrepeso.")
    
else:
    
    print(f"{nome}, seu IMC é {round(imc)}, você está obeso.")