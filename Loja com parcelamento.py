print("========= Placa de vídeo =========")
print("[1] - RTX 4090 - R$ 19.999,99")
print("[2] - RX 7900 - R$ 5.299,99")
print("[3] - RTX 3090 TI - R$ 16.900,99")
print("[4] - RX 580 - R$ 999,99")
print("[5] - Finalizar")
print("==================================")

rtx_4090 = 19999.99
rx_7900 = 5299.99
rtx_3090ti = 16900.99
rx_580 = 999.99

quantidade_rtx_4090 = 0
quantidade_rx_7900 = 0
quantidade_rtx_3090ti = 0
quantidade_rx_580 = 0

valor_final_rtx_4090 = 0
valor_final_rx_7900 = 0
valor_final_rtx_3090ti = 0
valor_final_rx_580 = 0

quantidade = 0
escolha = 0

while escolha != 5:

    escolha = int(input("Selecione a placa de video desejada: "))

    if escolha == 1:

        qtd_escolhida = int(input("Quantidade: "))
        qtd_parcela = int(input("Quantas vezes deseja parcelar: "))
        valor = qtd_escolhida * rtx_4090
        parcela = valor / qtd_parcela
        quantidade_rtx_4090 += qtd_escolhida
        valor_final_rtx_4090 += valor

        print(f"[1] - RTX 4090 = R$ {valor:.2f} em {qtd_parcela}x de R$ {parcela:.2f}")

    elif escolha == 2:

        qtd_escolhida = int(input("Quantidade: "))
        qtd_parcela = int(input("Quantas vezes deseja parcelar: "))
        valor = qtd_escolhida * rx_7900
        parcela = valor / qtd_parcela
        quantidade_rx_7900 += qtd_escolhida
        valor_final_rx_7900 += valor

        print(f"[2] - RX 7900 = R$ {valor:.2f} em {qtd_parcela}x de R$ {parcela:.2f}")

    elif escolha == 3:

        qtd_escolhida = int(input("Quantidade: "))
        qtd_parcela = int(input("Quantas vezes deseja parcelar: "))
        valor = qtd_escolhida * rtx_3090ti
        parcela = valor / qtd_parcela
        quantidade_rtx_3090ti += qtd_escolhida
        valor_final_rtx_3090ti += valor

        print(f"[3] - RTX 3090 TI = R$ {valor:.2f} em {qtd_parcela}x de R$ {parcela:.2f}")

    elif escolha == 4:

        qtd_escolhida = int(input("Quantidade: "))
        qtd_parcela = int(input("Quantas vezes deseja parcelar: "))
        valor = qtd_escolhida * rx_580
        parcela = valor / qtd_parcela
        quantidade_rx_580 += qtd_escolhida
        valor_final_rx_580 += valor

        print(f"[4] - RX 580 = R$ {valor:.2f} em {qtd_parcela}x de R$ {parcela:.2f}")

print("========= Nota fiscal =========")

if quantidade_rtx_4090 > 0:

    print(f"[1] - RTX 4090 | R$ {valor_final_rtx_4090} | QT: {quantidade_rtx_4090}")

if quantidade_rx_7900 > 0:

    print(f"[2] - RX 7900 | R$ {valor_final_rx_7900} | QT: {quantidade_rx_7900}")

if quantidade_rtx_3090ti > 0:

    print(f"[3] - RTX 3090 TI | R$ {valor_final_rtx_3090ti} | QT: {quantidade_rtx_3090ti}")

if quantidade_rx_580 > 0:

    print(f"[4] - RX 580 | R$ {valor_final_rx_580} | QT: {quantidade_rx_580}")

print("=============================")