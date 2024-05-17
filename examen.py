import unittest

def mi_funcion(x):
    # Tu lógica aquí
    for i in range(3):
        if x > i:
            print(f"{x} es mayor que {i}")
        else:
            print(f"{x} no es mayor que {i}")

    if x == 1:
        print("Caso 1")
    elif x == 2:
        print("Caso 2")
    else:
        print("Caso 3")

    return True

class TestMiFuncion(unittest.TestCase):
    def test_mi_funcion_case_1(self):
        self.assertTrue(mi_funcion(1))
        # caso 1

    def test_mi_funcion_case_2(self):
        self.assertTrue(mi_funcion(2))
        # caso 2

    def test_mi_funcion_case_3(self):
        self.assertTrue(mi_funcion(3))
        # caso 3

if __name__ == '__main__':
    unittest.main()
