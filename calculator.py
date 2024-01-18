import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora em Python")
        self.geometry("500x500")

        self.resultado_var = tk.StringVar()
        self.resultado_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Visor
        visor = tk.Entry(self, textvariable=self.resultado_var, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, justify="right")
        visor.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (texto, linha, coluna) in botoes:
            tk.Button(self, text=texto, command=lambda t=texto: self.clicar(t), height=2, width=5).grid(row=linha, column=coluna)

    def clicar(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(str(resultado))
            except Exception as e:
                self.resultado_var.set("Erro")
        elif valor == "C":
            self.resultado_var.set("0")
        else:
            if self.resultado_var.get() == "0":
                self.resultado_var.set(valor)
            else:
                self.resultado_var.set(self.resultado_var.get() + valor)

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.mainloop()
