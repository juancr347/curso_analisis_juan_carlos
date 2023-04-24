prices = [10, 20, 30, 40, 50]

prices_iva = []

def sumariva(price):
    return price * 1.21
print(f"El resultado es: {list(map(sumariva, prices))}")

