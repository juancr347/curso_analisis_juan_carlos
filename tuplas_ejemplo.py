lechuga = [3.99, 'verduras']
tomate = [4.99, 'verdura']
barcelo = [29.99, 'alcohol']
escalopines = [12.99,'carnes']
jack_daniels = [39.99, 'alcohol']
yogures = [4.50, 'lacteos']
queso = [14.99, 'lacteos']

productos = [lechuga, tomate, barcelo, escalopines, jack_daniels, yogures, queso]
        
fnames = ['Patricia', 'Jholman', 'Edu', 'Alan', 'Rafa']
    
    
     for producto in productos:   
    print(producto[0], producto[1])
    if producto[1] == 'alcohol':
        continue
    producto[0] = producto[0] * 0.10
    
    
    print(productos)