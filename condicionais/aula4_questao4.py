distancia = float(input("Distância da entrega em km: "))
peso = float(input("Peso do pacote em kg: "))

if distancia <= 100:
    valor_frete = peso * 1.00
elif distancia <= 300:
    valor_frete = peso * 1.50
else:
    valor_frete = peso * 2.00

if peso > 10:
    valor_frete += 10.00

print(f"Valor do frete: R${valor_frete:.2f}")
