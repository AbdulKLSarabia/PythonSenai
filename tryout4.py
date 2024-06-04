"""
Exercício 4: Média de Três Números
Peça ao usuário para digitar três números e calcule a média. Trate exceções para entradas inválidas.
Fórmula: media = (num1 + num2 + num3) / 3 
ValueError
ZeroDivisionError
"""
try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    media = (n1 + n2 + n3) / 3
    print(f"A média é: {media:.2f}")
except ValueError:
    print("Erro: Insira apenas números válidos.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
    
    
    
"""numeros = []
for i in range(3):
    try:
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    except ValueError:
        print(f"Erro: Insira apenas números válidos para o {i+1}º número.")

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"A média é: {media:.2f}")
else:
    print("Erro: Nenhum número válido foi inserido.")"""
