print('*** sistemas de inventarios ***')

inventario =[]

numero_productos = int(input('cuantos productos desea ingresar'))

for i in range(numero_productos):
    print(f'Ingresa los valores del producto {i+1}')
    nombre = input('Nombre : ')
    precio = float(input(('Precio : ')))
    cantidad = int(input('Cantidad : '))

    producto = {
        'id': i + 1,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(producto)
    print(f'\n')
print(f'\nInventario inicial : \n {inventario}')

buscar= int(input(f'\n ingrese el valor a buscar'))
producto_encontrado= None

for producto in inventario:
    if producto.get('id')== buscar:
        producto_encontrado=producto

        break
    if producto_encontrado != None:
        print(f'\n producto encontrado :\n {producto}')
        break
    else :
        print(f'\n el producto {buscar} no fue encontrado')