# --------------------------
# DEFINIÇÃO DE FUNÇÕES
# --------------------------
# Em Python, usamos 'def' para definir uma função. Uma função é um bloco de código reutilizável que executa uma tarefa específica.
# Aqui criamos a função 'exibir_menu()', que imprime o menu de opções sempre que for chamada.
def exibir_menu():
    # '\n' adiciona uma linha em branco antes do menu para melhor visualização
    print("\n===== MENU =====")
    print("1. Dizer olá")  # Opção para exibir uma saudação personalizada
    print("2. Fazer um cálculo")  # Opção para realizar um cálculo simples
    # Opção para contar de 1 até um número escolhido
    print("3. Contar até um número")
    print("4. Sair")  # Opção para encerrar o programa


# --------------------------
# LOOP PRINCIPAL DO PROGRAMA
# --------------------------
# O loop 'while True' mantém o programa rodando indefinidamente até que o usuário escolha sair.
while True:
    exibir_menu()  # Chamamos a função 'exibir_menu()' para mostrar as opções na tela
    # 'input()' recebe a escolha do usuário e armazena na variável 'opcao'
    opcao = input("Escolha uma opção: ")

    # --------------------------
    # OPÇÃO 1: DIZER OLÁ
    # --------------------------
    # 'if' verifica se o usuário digitou "1"
    if opcao == "1":
        # Pergunta o nome do usuário e armazena na variável 'nome'
        nome = input("Digite seu nome: ")
        # Exibe uma mensagem personalizada usando f-strings
        print(f"Olá, {nome}! Seja bem-vindo ao mundo da programação!")

    # --------------------------
    # OPÇÃO 2: FAZER UM CÁLCULO SIMPLES
    # --------------------------
    elif opcao == "2":
        print("Vamos fazer uma soma!")
        # Converte a entrada para número decimal (float)
        num1 = float(input("Digite o primeiro número: "))
        # Converte a entrada para número decimal (float)
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2  # Calcula a soma dos dois números e armazena em 'soma'
        # Exibe o resultado da soma na tela
        print(f"O resultado da soma é: {soma}")

    # --------------------------
    # OPÇÃO 3: CONTAR ATÉ UM NÚMERO ESCOLHIDO
    # --------------------------
    elif opcao == "3":
        # Converte a entrada para um número inteiro
        limite = int(input("Até que número você quer contar? "))
        for i in range(1, limite + 1):  # 'for' cria um loop que vai de 1 até 'limite'
            # 'end=" "' faz com que os números sejam impressos na mesma linha, separados por espaço
            print(i, end=" ")
        print()  # Pula uma linha ao final da contagem para melhor visualização

    # --------------------------
    # OPÇÃO 4: SAIR DO PROGRAMA
    # --------------------------
    elif opcao == "4":
        print("Saindo do programa... Até logo!")
        break  # 'break' encerra o loop 'while', finalizando o programa

    # --------------------------
    # OPÇÃO INVÁLIDA
    # --------------------------
    # Caso o usuário digite um número que não esteja no menu, mostramos uma mensagem de erro.
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 4.")
