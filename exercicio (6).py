alunos = [
    {'nome': 'Alice', 'nota': 8.5},
    {'nome': 'Bob', 'nota': 5.0},
    {'nome': 'Carol', 'nota': 7.2},
    {'nome': 'David', 'nota': 4.8}
]

for aluno in alunos:
    nome = aluno['nome']
    nota = aluno['nota']
    situacao = "aprovado" if nota >= 6 else "reprovado"
    mensagem = f"{nome} obteve nota {nota:.1f} e está {situacao}."
    print(mensagem)