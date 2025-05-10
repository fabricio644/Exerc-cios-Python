x = int(input("A partir de qual número: "))
y = int(input("Até quantos: "))


if y >= 1 and x >= 1 and x <= y:
    while x <= y:
        print(x)
        x += 1

else:
    print("Por favor digite números valídos.")