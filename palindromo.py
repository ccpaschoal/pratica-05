def eh_palindromo(texto: str) -> str:

    import re
    
    # Remove caracteres não alfanuméricos e converte para minúsculas
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


# Solicitando a palavra ou frase do usuário
entrada = input("Digite uma palavra ou frase: ")

# Verificando e exibindo o resultado
resultado = eh_palindromo(entrada)
print(f"A frase/palavra '{entrada}' é palíndromo? {resultado}")
