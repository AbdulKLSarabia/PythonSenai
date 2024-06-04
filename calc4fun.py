def adicao (a,b):
    return a + b

def subtrair (a,b):
    return a - b    

def multiplicar (a,b):
    return a * b

def divisao (a,b):
    return a / b

def main():
    print("Calculadora simples")
    print("Selecione a operação")
    print("1 Adição")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão ")


escolha = input("Digite sua escolha 1, 2, 3 ou 4: ")

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))

if escolha == '1':
    print("O resultado da Adição é ", adicao(numero1, numero2) )

elif escolha == '2':
    print("O resultado da Subtração é: ", subtrair(numero1, numero2) )

elif escolha == '3':
    print("O resultado da Multiplicação é: ", multiplicar(numero1, numero2) )
    
elif escolha == '4':
    print("O resultado da Divisão é: ", divisao(numero1, numero2) )

else: 
    print("Escolha invalida!")

