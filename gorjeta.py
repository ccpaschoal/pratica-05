def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100.0)

# Solicitando os valores ao usuário
valor_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta desejada (ex: 15 para 15%): "))

# Calculando e exibindo a gorjeta
gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"A gorjeta a ser deixada é: R${gorjeta:.2f}")