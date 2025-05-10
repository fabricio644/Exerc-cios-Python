idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")

print(f"Olá, {nome}.")

if idade >= 18:
    print(f"A idade informada é {idade}, você é maior de idade.")

if idade >= 18 and idade < 70:
    print(f"A idade informada é {idade}, você é obrigado a votar.")

elif idade <= 15:
    print(f"A idade informada é {idade}, você não pode votar.")

elif idade >= 16 or idade <= 17 and idade >= 70:
    print(f"A idade informada é {idade}, você pode votar, porem é facultativo.")




