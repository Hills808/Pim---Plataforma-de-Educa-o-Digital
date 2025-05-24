import tkinter as tk
from tkinter import messagebox, ttk
import json
import re
import webbrowser

AULAS = [
    {
        "titulo": "Aula 1: print()",
        "conteudo": "A função print() serve para mostrar informações na tela.\nExemplo:\nprint('Olá, mundo!')",
        "video": "https://www.youtube.com/watch?v=31llNGKWDdo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=6"
    },
    {
        "titulo": "Aula 2: Variáveis",
        "conteudo": "Variáveis armazenam valores. Exemplo:\nnome = \"Ana\"\nidade = 20\nprint(nome, idade)",
        "video": "https://www.youtube.com/watch?v=p1jB2xQuXFU&t=314s"
    },
    {
        "titulo": "Aula 3: if/else",
        "conteudo": "Usado para tomar decisões. Exemplo:\nif idade >= 18:\n    print(\"Maior de idade\")\nelse:\n    print(\"Menor de idade\")",
        "video": "https://www.youtube.com/watch?v=K10u3XIf1-Q"
    },
    {
        "titulo": "Aula 4: loops",
        "conteudo": "Usado para repetir ações. Exemplo:\nfor i in range(5):\n    print(i)",
        "video": "https://www.youtube.com/watch?v=cL4YDtFnCt4&t=1559s"
    }
]

ARQUIVO = "usuarios.json"


def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)


class SistemaEnsino:
    def __init__(self):
        self.usuarios = carregar_usuarios()
        self.usuario_logado = None
        self.janela = tk.Tk()
        self.janela.title("Sistema Educacional")
        self.interface_login()
        self.janela.mainloop()

    def limpar_janela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def interface_login(self):
        self.limpar_janela()
        tk.Label(self.janela, text="Email ou Nome").pack()
        email_entry = tk.Entry(self.janela)
        email_entry.pack()

        tk.Label(self.janela, text="Senha").pack()
        senha_entry = tk.Entry(self.janela, show="*")
        senha_entry.pack()

        def login():
            email = email_entry.get().strip()
            senha = senha_entry.get().strip()
            for u in self.usuarios:
                if (u["email"] == email or u["nome"] == email) and u["senha"] == senha:
                    self.usuario_logado = u
                    self.interface_principal()
                    return
            messagebox.showerror("Erro", "Credenciais inválidas.")

        tk.Button(self.janela, text="Entrar", command=login).pack(pady=5)
        tk.Button(self.janela, text="Cadastrar",
                  command=self.interface_cadastro).pack()

    def interface_cadastro(self):
        self.limpar_janela()
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
                messagebox.showerror("Erro", "Dados inválidos.")
                return
            if any(u["email"] == email for u in self.usuarios):
                messagebox.showerror("Erro", "Email já cadastrado.")
                return

            self.usuarios.append(
                {"nome": nome, "idade": idade, "email": email, "senha": senha})
            salvar_usuarios(self.usuarios)
            messagebox.showinfo("Sucesso", "Cadastro realizado.")
            self.interface_login()

        tk.Button(self.janela, text="Salvar", command=cadastrar).pack(pady=5)
        tk.Button(self.janela, text="Voltar",
                  command=self.interface_login).pack()

    def interface_principal(self):
        self.limpar_janela()
        notebook = ttk.Notebook(self.janela)
        notebook.pack(expand=True, fill="both")

        frame_aulas = tk.Frame(notebook)
        frame_exercicios = tk.Frame(notebook)

        notebook.add(frame_aulas, text="Aulas")
        notebook.add(frame_exercicios, text="Exercícios")

        # Mostrar aulas
        for aula in AULAS:
            f = tk.Frame(frame_aulas)
            f.pack(pady=5, anchor="w", fill="x")
            tk.Label(f, text=aula["titulo"], font=(
                "Arial", 10, "bold")).pack(anchor="w")
            tk.Label(f, text=aula["conteudo"], justify="left").pack(
                anchor="w", padx=10)
            tk.Button(f, text="Ver vídeo", command=lambda l=aula["video"]: webbrowser.open(
                l)).pack(anchor="w", pady=2)

        # Exercícios com múltipla escolha
        exercicios_mcq = [
            {
                "pergunta": "O que o comando print() faz?",
                "opcoes": [
                    "A) Recebe dados do usuário",
                    "B) Exibe uma mensagem na tela",
                    "C) Armazena valores em variáveis",
                    "D) Cria uma estrutura de repetição"
                ],
                "correta": "B"
            },
            {
                "pergunta": "Como declaramos uma variável em Python?",
                "opcoes": [
                    "A) var nome = valor",
                    "B) nome := valor",
                    "C) nome = valor",
                    "D) declare nome valor"
                ],
                "correta": "C"
            },
            {
                "pergunta": "Qual palavra usamos para condição?",
                "opcoes": [
                    "A) for",
                    "B) else",
                    "C) while",
                    "D) if"
                ],
                "correta": "D"
            },
            {
                "pergunta": "Qual comando usamos para repetir algo?",
                "opcoes": [
                    "A) repeat",
                    "B) loop",
                    "C) for",
                    "D) if"
                ],
                "correta": "C"
            }
        ]

        for ex in exercicios_mcq:
            f = tk.Frame(frame_exercicios, relief=tk.RIDGE, borderwidth=2)
            f.pack(padx=10, pady=5, fill="x")

            tk.Label(f, text=ex["pergunta"], font=("Arial", 10, "bold"), anchor="w").pack(
                anchor="w", padx=5, pady=3)

            var = tk.StringVar(value="")

            for opcao in ex["opcoes"]:
                letra = opcao[0]
                tk.Radiobutton(f, text=opcao, variable=var,
                               value=letra).pack(anchor="w", padx=20)

            def verificar(var=var, correta=ex["correta"]):
                resp = var.get()
                if resp == correta:
                    messagebox.showinfo("Correto", "Resposta correta!")
                else:
                    messagebox.showerror(
                        "Errado", f"Resposta incorreta! A resposta correta é '{correta}'.")

            tk.Button(f, text="Verificar resposta",
                      command=verificar).pack(pady=5)


if __name__ == "__main__":
    SistemaEnsino()
