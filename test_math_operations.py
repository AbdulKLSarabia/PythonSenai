import math_operations

def test_multiplicacao():
    assert math_operations.multiplicacao(2, 3) == 6
    assert math_operations.multiplicacao(0, 5) == 0
    assert math_operations.multiplicacao(-4, 2) == -8

def test_divisao():
    assert math_operations.divisao(10, 2) == 5
    assert math_operations.divisao(8, 4) == 2
    assert math_operations.divisao(15, 3) == 5

def test_divisao_por_zero():
    try:
        math_operations.divisao(10, 0)
    except ValueError as e:
        assert str(e) == "Não é possível dividir por zero."
    else:
        raise AssertionError("A exceção não foi lançada.")