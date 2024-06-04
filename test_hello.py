import pytest #Importar o Módulo pytest
from hello import add, subtract #Importar Funções do Módulo hello
 
def test_add(): #Definir o Teste test_add:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
 
def test_subtract(): #Definir o Teste test_subtract
    assert subtract(3, 2) == 1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0