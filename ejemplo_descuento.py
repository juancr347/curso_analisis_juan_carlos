productos = [lechuga, tomate, barcelo, escalopines, jack_daniels, yogures, queso] 

for producto in productos:   
    
    if producto[1] == 'alcohol':
        continue
    producto[0] = producto[0] * 0.10
    
    
    print(productos)       