import random

numero_secreto = random.randint(1,10)
contagem_tentativas = 0
numero = 0

print("========== JOGO ADVINHAÇÃO ==========")
print("Advinhe o número secreto (1 até 10)")

while numero != numero_secreto:

    numero = int(input("Digite sua tentativa: "))
    contagem_tentativas = contagem_tentativas + 1
    
    if numero == numero_secreto:
        
        print("Parabens, você acertou o número secreto !") 
        print(f"Você precisou de {contagem_tentativas} tentativas.")
        
        break
    
    elif numero > numero_secreto:
        
        print("O número está maior que o número secreto.")
        
    else:
        
        print("O número está menor que o número secreto.")