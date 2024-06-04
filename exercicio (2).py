nome = "Alice"
idade = 30
saldo = 1500.75

frase_concatenada = "Olá, meu nome é " + nome + ", tenho " + str(idade) + " anos e meu saldo é R$" + str(saldo) + "."
print(frase_concatenada)

frase_interpolação = f"Olá, meu nome é {nome}, tenho {idade} anos e meu saldo é R${saldo:.2f}."
print(frase_interpolação)

frase_format = "Olá, meu nome é {}, tenho {} anos e meu saldo é R${:.2f}.".format(nome, idade, saldo)
print(frase_format)