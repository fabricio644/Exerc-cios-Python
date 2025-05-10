kmPecorrido = float(input("Quantos KM você pecorreu: "))
diasAlugado = int(input("Quantos dias você alugou o carro: "))
total = (diasAlugado * 90) + (kmPecorrido * 0.20)

print("========== NOTA FISCAL ==========")
print(f"[1] - KM = R$ {(kmPecorrido * 0.20)}")
print(f"[2] - DIAS = R$ {(diasAlugado * 90)}")
print("=================================")
print(f"TOTAL = R$ {total}")
