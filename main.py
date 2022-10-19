# Contar cuántas veces se repitió cada elemento de una lista.

import unittest

def contar_elementos(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

class TestList(unittest.TestCase):
    def test_1(self):
        dic = contar_elementos([1, 1, 1, 2, 3, 3])
        self.assertEqual(dic, {1: 3, 2: 1, 3: 2})
    
    def test_2(self):
        dic = contar_elementos(["a", "b", "c", "c", "d", "d", "d"])
        self.assertEqual(dic, {"a": 1, "b": 1, "c": 2, "d": 3})
    
    def test_3(self):
        dic = contar_elementos([1, 1, 1, 2, 3, 3, "a", "b", "c", "c", "d", "d", "d"])
        self.assertEqual(dic, {1: 3, 2: 1, 3: 2, "a": 1, "b": 1, "c": 2, "d": 3})

if __name__ == '__main__':
    unittest.main()