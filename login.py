import tkinter as tk
from tkinter import messagebox

class TelaLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tela de Login em Python")
        self.geometry("500x500")

        self.criar_widgets()

    def criar_widgets(self):
        # Rótulos e campos de entrada
        tk.Label(self, text="User:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        tk.Label(self, text="Password:").grid(row=1, column=0, sticky="e", padx=10, pady=5)

        self.nome_usuario_entry = tk.Entry(self)
        self.nome_usuario_entry.grid(row=0, column=1, padx=10, pady=5)

        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botão de login
        tk.Button(self, text="Login", command=self.realizar_login).grid(row=2, column=0, columnspan=2, pady=10)

    def realizar_login(self):
        # Substitua esta lógica pelo seu próprio sistema de autenticação
        nome_usuario = self.nome_usuario_entry.get()
        senha = self.senha_entry.get()

        # Exemplo simples de autenticação
        if nome_usuario == "usuario" and senha == "senha":
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

if __name__ == "__main__":
    tela_login = TelaLogin()
    tela_login.mainloop()

