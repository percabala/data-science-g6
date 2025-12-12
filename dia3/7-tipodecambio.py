TIPO_DE_CAMBIO = 3.0 
print(f"Tipo de cambio: 1 Dólar ($) = {TIPO_DE_CAMBIO} Soles (S/)\n")
print("Selecciona la conversión que deseas realizar:")
print("1: Soles (S/) a Dólares ($)")
print("2: Dólares ($) a Soles (S/)")
opcion = input("Elija una opcion: ")
cantidad = float(input("\nIngresa la cantidad a convertir: "))
if opcion == '1':
    resultado = cantidad / TIPO_DE_CAMBIO
    moneda_origen = "Soles (S/)"
    moneda_destino = "Dólares ($)"
elif opcion == '2':
    resultado = cantidad * TIPO_DE_CAMBIO
    moneda_origen = "Dólares ($)"
    moneda_destino = "Soles (S/)" 
else:
    resultado = 0
    print("\n Opción no válida.")
    exit()
if resultado > 0:
    print(f"\n Resultado de la conversión:")
    print(f"{cantidad:.2f} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}")