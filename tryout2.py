"""
Exercício 2: Divisão com Tratamento de Exceção
Peça ao usuário para digitar dois números e tente dividi-los. Se ocorrer uma divisão por zero, exiba uma mensagem de erro.
ZeroDivisionError
"""

try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f"Resultado da divisão: {resultado}")
except ValueError:
    print("Erro: Digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
finally:
    print("FIM!!")