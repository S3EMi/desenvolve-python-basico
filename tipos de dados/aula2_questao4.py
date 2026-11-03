# Reescrevendo usando apenas duas variáveis
juros = 1.01
saldo = 500.0

# Acumulando os juros mês a mês na própria variável de saldo
saldo = saldo * juros # Mês 1
saldo = saldo * juros # Mês 2
saldo = saldo * juros # Mês 3

print("Após 3 meses meu novo saldo é")
print(saldo)
