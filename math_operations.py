def multiplicacao(a, b):
    """
    Retorna o resultado da multiplicação entre a e b.
    """
    return a * b

def divisao(a, b):
    """
    Retorna o resultado da divisão entre a e b.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b