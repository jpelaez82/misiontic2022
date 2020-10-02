def parqueadero_buses(cantidad_buses, numero_bus):
    # Evaluar cantidad de buses -> multiplo de 3
    p = cantidad_buses % 3 == 0
    q = numero_bus <= cantidad_buses and numero_bus > 0
    # Validar tipo de datos que ingresa
    r = isinstance(numero_bus, int)
    s = isinstance(cantidad_buses, int)

    # Validacion
    if p and q and r and s:
        # Primer lote
        if numero_bus <= cantidad_buses / 3:
            lote = 1
        else:
            # Segundo Lote
            if numero_bus <= cantidad_buses * 2/3:
                lote = 2
            else:
                # Tercer Lote
                lote = 3
    else:
        lote = "No se puede parquear aqui"
    return lote

# Comprobacion
print(parqueadero_buses(100, 1))
print(parqueadero_buses(99, -3))
print(parqueadero_buses(102, 40))
print(parqueadero_buses(30, 40))
print(parqueadero_buses(100, 33))
    