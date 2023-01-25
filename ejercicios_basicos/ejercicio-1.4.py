precio_venta = float(input('el costo del articulo vendido es de: '))
diner_a_pagar  = float(input('el cliente va a pagar con: '))


if diner_a_pagar > precio_venta:
    print(f'el cambio correspondiente al cliente es de {diner_a_pagar - precio_venta}')
elif diner_a_pagar < precio_venta:
    print(f'la cantidad que falta a abonar para comprar el producto es de {precio_venta - diner_a_pagar }')
elif diner_a_pagar == precio_venta:
    print('usted pago justo')
