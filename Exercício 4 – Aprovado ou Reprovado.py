nota1 = int(input("Digite a nota de Artes: "))
nota2 = int(input("Digite a nota de Ciências: "))
nota3 = int(input("Digite a nota de Matematica: "))
nota4 = int(input("Digite a nota de Português: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"Sua média foi {media:.2f}, portanto você está aprovado.")

else:
    print(f"Sua média foi {media:.2f}, você está reprovado.")
