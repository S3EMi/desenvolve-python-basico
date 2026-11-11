N = int(input())
soma = 0
cont = 0

while cont < N:
    idade = int(input())
    soma += idade
    cont += 1

if N > 0:
    media = soma / N
    print(media)
