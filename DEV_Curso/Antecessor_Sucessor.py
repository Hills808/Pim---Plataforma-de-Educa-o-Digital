n = int(input("Digite um numero: "))
a = n - 1
s = n + 1
print("O antecessor de {} é {} e o sucessor é {}".format(n, a, s))


# pode usar assim com apenas uma variavel, fazendo o (n-1) e (n+1) no .format.
# Porem isso só é valido quando não for precisar do valor das variaveis, (a) e (s)
# n = int(input("Digite um numero: "))
# print("O antecessor de {} é {} e o sucessor é {}".format(n, (n-1), (n+1)))
