# Solicita ao usuário para inserir uma nota
nota = float(input("Digite a nota de 0 a 100: "))

# Classifica a nota
if 90 <= nota <= 100:
    letra = "A"
elif 80 <= nota < 90:
    letra = "B"
elif 70 <= nota < 80:
    letra = "C"
elif 60 <= nota < 70:
    letra = "D"
else:
    letra = "F"

print(f"Você tirou um {letra}.")