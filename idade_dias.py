def calcula_idade_em_dias(ano_nascimento: int) -> int:
   
    from datetime import date
    data_atual = date.today()
    
    # Considerando o nascimento em 1º de janeiro do ano fornecido
    data_nascimento = date(ano_nascimento, 1, 1)
    return (data_atual - data_nascimento).days


# Solicitando o ano de nascimento do usuário
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Calculando e exibindo a idade em dias
idade_dias = calcula_idade_em_dias(ano_nascimento)
print(f"Você tem aproximadamente {idade_dias} dias de vida.")
