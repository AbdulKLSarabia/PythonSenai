"""
Exercício 1: Capturando Erro de Entrada de Inteiro
Peça ao usuário para digitar um número inteiro. Se a entrada não for um número inteiro, exiba uma mensagem de erro.
ValueError
"""

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: A entrada não é um número inteiro válido.")