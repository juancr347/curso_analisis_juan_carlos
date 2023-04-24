def saludar2(nombre= 'juan', edad=30):
    print(f" hola soy {nombre} con edad {edad}")
    
    
saludar2()
saludar2("antonio")
saludar2("albert", 40)


def suma(num1, num2):
    """_summary_

    Args:
        num1 (number): numero entero positivo mayor que cero
        num2 (number): numero entero positivo mayor que cero
    """
    
    return num1 + num2

print(suma(5, 5))

saludo = saludar("Mike-, 35")
print(saludo)

suma = lambda num1, num2: num1 + num2

suma = lambda num1, num2: num1 * num2

print(sumar(5, 5))