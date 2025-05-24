import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import re
import webbrowser

usuarios_arquivo = "usuarios.json"

aulas = [
    {
        "titulo": "Aula 1: print()",
        "conteudo": "A função print() serve para mostrar informações na tela.\nExemplo:\nprint('Olá, mundo!')",
        "video": "https://www.youtube.com/watch?v=8mAITcNt710"
    },
    {
        "titulo": "Aula 2: Variáveis",
        "conteudo": "Variáveis armazenam valores para usar no programa.\nExemplo:\nx = 10\nprint(x)",
        "video": "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ"
    },
    {
        "titulo": "Aula 3: if/else",
        "conteudo": "Estruturas condicionais executam código dependendo de uma condição.\nExemplo:\nif x > 5:\n    print('Maior que 5')\nelse:\n    print('Menor ou igual a 5')",
        "video": "https://www.youtube.com/watch?v=Z8SuSfd8vYU"
    },
    {
        "titulo": "Aula 4: Loops",
        "conteudo": "Loops repetem comandos várias vezes.\nExemplo:\nfor i in range(3):\n    print(i)",
        "video": "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ"
    }
]

exercicios = [
    {
        "pergunta": "Escreva um código que exibe 'Olá, mundo!' na tela:",
        "resposta": "print('Olá, mundo!')"
    },
    {
        "pergunta": "Crie uma variável chamada idade e atribua o valor 20:",
        "resposta": "idade = 20"
    },
    {
        "pergunta": "Complete: if idade >= 18:\n_____('Maior de idade')",
        "resposta": "print('Maior de idade')"
    },
    {
        "pergunta": "Crie um loop que imprima os números de 0 a 2:",
        "resposta": "for i in range(3): print(i)"
    }
]


def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def carregar_usuarios():
    try:
        with open(usuarios_arquivo, "r") as f:
            return json.load(f)
    except:
        return []


def salvar_usuarios(lista):
    with open(usuarios_arquivo, "w") as f:
        json.dump(lista, f, indent=4)


class Sistema:
    def __init__(self):
        self.usuarios = carregar_usuarios()
        self.usuario_atual = None
        self.janela = tk.Tk()
        self.janela.title("Sistema de Ensino Python")
        self.tela_login()
        self.janela.mainloop()

    def limpar_tela(self):
        for w in self.janela.winfo_children():
            w.destroy()

    def tela_login(self):
        self.limpar_tela()
        tk.Label(self.janela, text="Email ou Nome").pack()
        entrada_email = tk.Entry(self.janela)
        entrada_email.pack()

        tk.Label(self.janela, text="Senha").pack()
        entrada_senha = tk.Entry(self.janela, show="*")
        entrada_senha.pack()

        def entrar():
            email = entrada_email.get().strip()
            senha = entrada_senha.get().strip()
            for u in self.usuarios:
                if (u["email"] == email or u["nome"] == email) and u["senha"] == senha:
                    self.usuario_atual = u
                    self.tela_principal()
                    return
            messagebox.showerror("Erro", "Login inválido.")

        tk.Button(self.janela, text="Entrar", command=entrar).pack(pady=5)
        tk.Button(self.janela, text="Cadastrar",
                  command=self.tela_cadastro).pack()

    def tela_cadastro(self):
        self.limpar_tela()
        labels = ["Nome", "Idade", "Email", "Senha"]
        entradas = {}

        for l in labels:
            tk.Label(self.janela, text=l).pack()
            entradas[l] = tk.Entry(
                self.janela, show="*" if l == "Senha" else "")
            entradas[l].pack()

        def cadastrar():
            nome = entradas["Nome"].get().strip()
            idade = entradas["Idade"].get().strip()
            email = entradas["Email"].get().strip()
            senha = entradas["Senha"].get().strip()

            if not nome or not idade.isdigit() or not validar_email(email) or len(senha) < 4:
                messagebox.showerror("Erro", "Preencha os dados corretamente.")
                return
            if any(u["email"] == email for u in self.usuarios):
                messagebox.showerror("Erro", "Email já cadastrado.")
                return

            self.usuarios.append(
                {"nome": nome, "idade": idade, "email": email, "senha": senha})
            salvar_usuarios(self.usuarios)
            messagebox.showinfo("Sucesso", "Cadastro feito com sucesso!")
            self.tela_login()

        tk.Button(self.janela, text="Salvar", command=cadastrar).pack(pady=5)
        tk.Button(self.janela, text="Voltar", command=self.tela_login).pack()

    def tela_principal(self):
        self.limpar_tela()
        notebook = ttk.Notebook(self.janela)
        notebook.pack(expand=True, fill="both")

        frame_aulas = tk.Frame(notebook)
        frame_exercicios = tk.Frame(notebook)

        notebook.add(frame_aulas, text="Aulas")
        notebook.add(frame_exercicios, text="Exercícios")

        for aula in aulas:
            f = tk.Frame(frame_aulas)
            f.pack(anchor="w", pady=5)
            tk.Label(f, text=aula["titulo"]).pack(anchor="w")
            tk.Label(f, text=aula["conteudo"]).pack(anchor="w")
            tk.Button(f, text="Assistir Vídeo", command=lambda link=aula["video"]: webbrowser.open(
                link)).pack(anchor="w", pady=2)

        for ex in exercicios:
            f = tk.Frame(frame_exercicios)
            f.pack(anchor="w", pady=5)
            tk.Label(f, text=ex["pergunta"]).pack(anchor="w")
            entrada = tk.Entry(f, width=60)
            entrada.pack(side=tk.LEFT)

            def verificar(entry=entrada, resp=ex["resposta"]):
                resposta_usuario = entry.get().strip().replace(" ", "").lower()
                resposta_certa = resp.strip().replace(" ", "").lower()
                if resposta_usuario == resposta_certa:
                    messagebox.showinfo("Correto", "Resposta correta!")
                else:
                    messagebox.showerror(
                        "Errado", f"Resposta incorreta.\nEsperado: {resp}")

            tk.Button(f, text="Verificar", command=verificar).pack(
                side=tk.LEFT, padx=5)


Sistema()
