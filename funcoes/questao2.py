import random
import math

n = int(input("Digite a quantidade de valores (n): "))

soma = 0
for _ in range(n):
    soma += random.randint(0, 100)

raiz = math.sqrt(soma)
print(f"A raiz quadrada da soma é: {raiz:.2f}")
