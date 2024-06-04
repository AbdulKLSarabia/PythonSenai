def obter_numero_valido():
    while True:
        try:
            entrada = input("Digite um número: ")
            numero = float(entrada)
            return numero
        except ValueError:
            print("Erro: Insira apenas números válidos.")

# Solicitação do número ao usuário
numero_digitado = obter_numero_valido()
print(f"Você digitou o número: {numero_digitado:.2f}")