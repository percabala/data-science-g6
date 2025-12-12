import os
# CALCULADORA COMPLETA CON PYTHON
salir = "no"
while(salir == "no"):
    os.system("clear")
    # ENTRADA
    print("=============OPCIONES==============")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (x)")
    print("4. División (/)")
    print("5. tabla de multiplicar")
    opcion = int(input("Seleccione la opcion que desea): "))
    if opcion == 5:
        tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
        for contador in range(1,13,1):
            resultado = tabla * contador
            print(f"{tabla} x {contador} = {resultado}")
    elif(opcion >= 1 and opcion < 5):
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: ")) 
        # PROCESO
        if opcion == 1:
            operacion = "suma"
            resultado = numero1 + numero2
        elif opcion == 2:
            operacion = "resta"
            resultado = numero1 - numero2
        elif opcion == 3:
            operacion = "multiplicación"
            resultado = numero1 * numero2
        elif opcion == 4:
            operacion = "división"
            resultado = numero1 / numero2
        else:
            print("Operación no válida")
            exit()
        # SALIDA
        print(f"La {operacion} de {numero1} y {numero2} = {resultado}")

    salir = input("¿Desea salir de la calculadora? (si/no): ")
    if salir == "si":
        break