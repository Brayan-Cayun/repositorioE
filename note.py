def menu():
    cant = 40
    venta = 0
    devolucion = 0 
    print('''NOTEBOOKS MENÚ
1. Cantidad de notebooks
2. Venta de notebook
3. Devolución de notebook
4. Cantidad de notebooks vendidas
0. Salir''')
    while True:
        try:
            opc = int(input('Ingrese una opción: '))
            if opc == 0:
                print('Programa finalizado.')
                break
            elif opc == 1:
                print(f'La cantidad de notebooks disponibles es: {cant}')
            elif opc == 2:
                vent = int(input('Ingrese la cantidad de notebooks a vender: '))
                if vent <= cant:
                    cant -= vent
                    venta += vent
                    print(f'Se vendieron un total de {vent} notebooks.')
            elif opc == 3:
                devo = int(input('Ingrese la cantidad de notebooks a devolver: '))
                if devo <= venta:
                    cant += devo
                    devolucion += devo
                    venta -= devo
            elif opc == 4: print(f'La cantidad de notebooks vendidas es: {venta}')
            else: print('Opcion no valida, Intente de nuevo!')
        except ValueError: print('Ingrese un valor valido!')
menu()