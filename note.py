def menu():
    cant = 40
    venta = 0
    devolucion = 0
    print('''NOTEBOOKS MENÚ
1. Cantidad de notebooks
2. Venta de notebook
3. Devolución de notebook
4. Salir''')
while True:
    opc = int(input('Ingrese una opción: '))
    if opc == 0:
        print('Programa finalizado.')
        break
    elif opc == 1:
        print(f'La cantidad de notebooks disponibles es: {cant}')
        
        