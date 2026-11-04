classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower().strip()
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

guerreiro_valido = (classe == "guerreiro") and (forca >= 15) and (magia <= 10)
mago_valido = (classe == "mago") and (forca <= 10) and (magia >= 15)
arqueiro_valido = (classe == "arqueiro") and (5 < forca <= 15) and (5 < magia <= 15)

consistente = guerreiro_valido or mago_valido or arqueiro_valido

print("Pontos de atributo consistentes com a classe escolhida:", consistente)
