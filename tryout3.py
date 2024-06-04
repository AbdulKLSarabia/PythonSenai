"""
Exercício 3: Conversão de String para Float
Peça ao usuário para digitar um número. Converta a entrada para um float e exiba o resultado. Se a conversão falhar, exiba uma mensagem de erro.
ValueError
"""

try:
    entrada = input("Digite um número: ")
    numero = float(entrada)
    print(f"O número digitado é: {numero}")
except ValueError:
    print("Erro: A entrada não é um número válido.")