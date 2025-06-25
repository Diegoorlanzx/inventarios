print('*** Sistemas de Inventarios ***')

inventario = []

numero_productos = int(input('¿Cuántos productos desea ingresar? '))

for i in range(numero_productos):
    print(f'\nIngresa los valores del producto {i + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    producto = {
        'id': i + 1,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(producto)

print('\nInventario inicial:')
for producto in inventario:
    print(producto)

buscar = int(input('\nIngrese el ID del producto a buscar: '))
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'\nProducto encontrado:\n{producto_encontrado}')
else:
    print('\nEl producto no fue encontrado.')
