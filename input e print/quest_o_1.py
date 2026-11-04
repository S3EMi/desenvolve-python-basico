# Lê o comprimento do terreno como inteiro
comprimento = int(input())
# Lê a largura do terreno como inteiro
largura = int(input())
# Lê o preço do metro quadrado como ponto flutuante
preco_m2 = float(input())
# Calcula a área multiplicando o comprimento pela largura
area_m2 = comprimento * largura
# Calcula o preço total multiplicando o preço do metro quadrado pela área
preco_total = preco_m2 * area_m2
# Imprime a mensagem formatada com a área e o valor total em reais com separador de milhar
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")