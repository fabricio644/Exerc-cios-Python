import tkinter as tk
from tkinter import messagebox

# Função para realizar as operações
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        oper = var_oper.get()

        if oper == 1:
            resultado = num1 + num2
            operacao = "Soma"
        elif oper == 2:
            resultado = num1 - num2
            operacao = "Subtração"
        elif oper == 3:
            if num2 == 0:
                raise ValueError("Não é possível dividir por zero!")
            resultado = num1 / num2
            operacao = "Divisão"
        elif oper == 4:
            resultado = num1 * num2
            operacao = "Multiplicação"
        elif oper == 5:
            resultado = "Operação finalizada"
            operacao = "Finalizando"
        else:
            resultado = "Escolha uma operação válida!"
            operacao = ""

        # Exibe o resultado
        messagebox.showinfo(f"Resultado da {operacao}", f"{operacao}: {resultado}")

    except ValueError as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

# Função para limpar os campos
def limpar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    var_oper.set(0)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Labels e campos de entrada para os números
label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Opcões de operações
var_oper = tk.IntVar()

label_oper = tk.Label(root, text="Escolha a operação:")
label_oper.pack()

# Botões de operação
operacoes = [
    ("Soma", 1),
    ("Subtração", 2),
    ("Divisão", 3),
    ("Multiplicação", 4),
    ("Finalizar", 5)
]

for texto, valor in operacoes:
    tk.Radiobutton(root, text=texto, variable=var_oper, value=valor).pack()

# Botões para calcular e limpar
btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack()

btn_limpar = tk.Button(root, text="Limpar", command=limpar)
btn_limpar.pack()

# Iniciar a interface gráfica
root.mainloop()
