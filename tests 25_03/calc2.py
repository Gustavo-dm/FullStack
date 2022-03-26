import abc
from unittest import TestCase,main
from webbrowser import Opera

class Calculator(object):
    def calc(self,val1,val2, operator):
        operatorFabric = OperatorFabric()
        operation = operatorFabric.create(operator)
        if operation:
            resultado = operation.execute(val1,val2)
            return resultado
        else:
            return 0

class OperatorFabric(object):
    def create(self, operator):
        match operator:
            case 'sum':
                return Sum()
            case 'sub':
                return Sub()
            case 'div':
                return Div()
            case 'mult':
                return Mult()

class Operation(metaclass =abc.ABCMeta):
    def execute(val1,val2):
        pass

class Sum(Operation):
    def execute(self,val1,val2):
        result = val1 + val2
        return result
class Sub(Operation):
    def execute(self,val1,val2):
        result = val1 - val2
        return result
class Div(Operation):
    def execute(self,val1,val2):
        result = val1 / val2
        return result
class Mult():
    def execute(self,val1,val2):
        result = val1 * val2
        return result


class Testes(TestCase):


    def test_sum(self):
        calculator = Calculator()
        res = calculator.calc(2,3,'sum')
        self.assertEqual(res,5)

    def test_sub(self):
        calculator = Calculator()
        res = calculator.calc(3,1,'sub')
   
        self.assertEqual(res,2)

    def test_div(self):
        calculator = Calculator()
        res = calculator.calc(10,5,'div')
   
        self.assertEqual(res,2)

    def test_mult(self):
        calculator = Calculator()
        res = calculator.calc(2,3,'mult')
      
        self.assertEqual(res,6)


if __name__ == '__main__':
    main()