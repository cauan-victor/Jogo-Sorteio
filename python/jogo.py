import tkinter as tk
from tkinter import messagebox
import random

class SorteioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorteio Aleatório")

        # Configuração da interface
        self.label_numero = tk.Label(self.master, text="Número Sorteado:", font=("Arial", 14))
        self.label_numero.pack(pady=10)

        self.numero_sorteado_var = tk.StringVar()
        self.numero_sorteado_entry = tk.Entry(self.master, textvariable=self.numero_sorteado_var, font=("Arial", 16), state="readonly", readonlybackground="white")
        self.numero_sorteado_entry.pack(pady=20)

        self.botao_sorteio = tk.Button(self.master, text="Sortear Número", command=self.sortear_numero, font=("Arial", 14))
        self.botao_sorteio.pack()

    def sortear_numero(self):
        numero_sorteado = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        self.numero_sorteado_var.set(numero_sorteado)
        messagebox.showinfo("Sorteio", f"Número sorteado: {numero_sorteado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SorteioApp(root)
    root.mainloop()
