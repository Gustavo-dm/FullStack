from unittest import TestCase, main
from numbers import Number


# def validate_cache(func, cache={}):
#     def validate_apply_cache(self, x, y=None):

#         chave = False

#         if y == None:
#             y = cache['value']
#             chave = True

#         if isinstance(x, Number) and isinstance(y, Number):
#             if chave:
#                 cache['value'] = func(self, y, x)
#             else:
#                 cache['value'] = func(self, x, y)
#             return cache['value']

#         else:
#             raise Exception('insira somente números')

#     return validate_apply_cache


class Calc:
#     @validate_cache
    def soma(self, x, y):
        return x + y

#     @validate_cache
    def mul(self, x, y):
            return x * y

#     @validate_cache
    def sub(self, x, y):
        return x - y

#     @validate_cache
    def div(self, x, y):
        return x / y


class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 2), 4)

    def test_soma_neg(self):
        self.assertEqual(self.calc.soma(-2, -3), -5)

    def test_soma_float(self):
        self.assertEqual(self.calc.soma(2.0, 1.0), 3.0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 2), 0)

    def test_sub_float(self):
        self.assertEqual(self.calc.sub(2.0, 2.0), 0)

    def test_soma_string(self):
        self.calc.soma('Salve Fessor', 'jaber')

    def test_sub_string(self):
        
        self.calc.sub('Salve Fessor', 'jaber')

    def test_mul(self):
        self.assertEqual(self.calc.mul(3, 3), 9)

    def test_mul_string(self):
   
        self.calc.mul(3, 'Salve Fessor')

    def test_div(self):
        self.assertEqual(self.calc.div(3, 3), 1)

    def test_div_string(self):

        self.calc.div(3, 'Salve Fessor')

   


if __name__ == '__main__':
    main()