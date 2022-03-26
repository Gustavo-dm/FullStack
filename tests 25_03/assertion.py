def soma(a,b):
   
    assert type(a) ==int
    assert type(b) ==int
    return a +b
    
try:
    resultado = soma('a', 'b')

except AssertionError as err:
        print(f'Erro {err}')