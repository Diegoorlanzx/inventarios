print('*** sistemas de inventarios ***')

inventario =[]

numero_productos = int(input('cuantos productos desea ingresar'))

for i in range(numero_productos):
    print(f'Ingresa los valores del producto {i+1}')
    nombre = input('Nombre : ')
    precio = float(input(('Precio : ')))
    cantidad = int(input('Cantidad : '))

    producto = {'id' : i+1, 'nombre' : {nombre}, 'precio' : {precio}, 'cantidad' : {cantidad}}
    inventario.append(producto)
print(f'\nInventario inicial : \n {inventario}')