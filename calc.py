from decimal import InvalidOperation
import math
from flask import Flask, render_template, request
from unittest import TestCase, main
app = Flask(__name__)
app.config.from_object(__name__)

class Calc:
    def ope(self, x, y, operation):
        match operation:
            case "Sum":
                result = x + y 
            case "Sub":
                result = x - y
            case "Multi":
                result = x * y
            case "Div":
                result = x / y
            case "Sqr":
                result = math.sqrt(x)
            case "Log":
                result = math.log(x,y)
            case "Pow":
                result = math.pow(x,y)

        return result
            
@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def show_result():
    var_1 = float(request.form.get("var_1"))
    var_2 = float(request.form.get("var_2"))
    operation = request.form.get("operation")
    calc = Calc()
    try:
        res = calc.ope(var_1,var_2,operation)
    except:
        res = "Error"
    finally:
            return render_template('result.html', res=res)

class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_soma(self):
        self.assertEqual(self.calc.ope(2, 2,"Sum"), 4)

    def test_soma_neg(self):
        self.assertEqual(self.calc.ope(-2, -3,"Sum"), -5)

    def test_soma_float(self):
        self.assertEqual(self.calc.ope(2.0, 1.0,"Sum"), 3.0)
    
    

    def test_sub(self):
        self.assertEqual(self.calc.ope(2, 2,"Sub"), 0)

    def test_sub_float(self):
        self.assertEqual(self.calc.ope(2.0, 2.0,"Sub"), 0)


    def test_mul(self):
        self.assertEqual(self.calc.ope(3, 3,"Multi"), 9)

    
    def test_div(self):
        self.assertEqual(self.calc.ope(3, 3,"Div"), 1)

  
    def test_div_byZero(self):
        self.assertRaises(ZeroDivisionError,self.calc.ope(3,0,"Div"))
   
    def test_sqr(self):
        self.assertEqual(self.calc.ope(9,0,"Sqr",),3)

    def test_log(self):
        self.assertEqual(self.calc.ope(9,2,"Log"),3.1699250014423126)
#não entendo o comportamento, mas os erros estão sendo tratados
    def test_log_baseZero(self):
        self.assertRaises(ValueError,self.calc.ope(9,0,"Log"))
    
    def test_pow(self):
        self.assertEqual(self.calc.ope(5,5,"Pow"),3125.0)

if __name__ == '__main__':
    app.run(debug=True)
    main()