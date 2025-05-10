oper = 0

while oper != 5:

    print("===== CALCULADORA =====")
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Divisão")
    print("[4] - Multiplicação")
    print("[5] - Finalizar")
    print("=======================")

    oper = int(input("Digite a operação a realizar: "))

    if oper == 1:

        print("=======================")
        print(f"Você escolheu {oper}, Soma")
        print("=======================")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("=======================")

        print(f"{num1} + {num2} = {(num1+num2)}") 

    if oper == 2:

        print("=======================")
        print(f"Você escolheu {oper}, Subtração")
        print("=======================")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("=======================")

        print(f"{num1} - {num2} = {(num1-num2)}")

    if oper == 3:

        print("=======================")
        print(f"Você escolheu {oper}, Divisão")
        print("=======================")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("=======================")

        print(f"{num1} / {num2} = {(num1/num2)}")     

    if oper == 4:
        
        print("=======================")
        print(f"Você escolheu {oper}, Multiplicação")
        print("=======================")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("=======================")

        print(f"{num1} * {num2} = {(num1*num2)}")  

    if oper == 5:
        
        print("=======================")
        print(f"Você escolheu {oper}, saindo!")
        print("=======================")



