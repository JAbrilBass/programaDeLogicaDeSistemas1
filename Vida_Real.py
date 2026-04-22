# Programa con problemas de la vida real

# Joan Mauricio Gutérrez Abril
def salidaAComer():     #Se define la función para calcular el pago de una cuenta en un restaurante, incluyendo la propina.

    print("=====================================")
    print("Salida a Comer")        # Se muestra un mensaje indicando que se ha seleccionado la opción de salida a comer.
    print("=====================================")

    pedidos = {}
    personas = int(input("Cuantas personas salieron a comer? "))    # Se solicita al usuario que ingrese el número de personas que salieron a comer y se almacena en la variable 'personas'.

    for i in range(personas):   # Se utiliza un bucle for para solicitar al usuario que ingrese el nombre y el precio de cada pedido. El bucle se ejecuta 3 veces, permitiendo ingresar 3 pedidos.
        nombre = input(f"Ingresa el nombre de la persona {i+1}: ")   # Se solicita al usuario que ingrese el nombre de la persona y se almacena en la variable 'nombre'.
        pedidos[nombre] = []  # Se solicita al usuario que ingrese el precio del pedido de la persona y se almacena en el diccionario 'pedidos' con el nombre como clave y el precio como valor.
    
        while True:    # Se utiliza un bucle while para permitir al usuario ingresar múltiples precios para cada persona. El bucle se ejecuta hasta que el usuario ingresa "fin".
            plato = input(f"¿Qué pidió {nombre}? ")
            costo = float(input(f"¿Cuánto costó el {plato}? "))
            pedidos[nombre].append((plato, costo))

            continuar = input("¿Agregar otro plato o bebida? (si/no): ")
            if continuar.lower() != "si":
                break
    
    print("Van a dividir la cuenta entre todos o cada quien va a pagar lo suyo?")   # Se solicita al usuario que ingrese si van a dividir la cuenta entre todos o si cada persona va a pagar lo suyo.
    division = input("Escribe 'dividir' para dividir la cuenta entre todos o 'individual' para que cada persona pague lo suyo: ")
    
    while True:    # Se utiliza un bucle while para verificar la elección del usuario. El bucle se ejecuta hasta que el usuario ingresa una opción válida ("dividir" o "individual").
        if division.lower() == "dividir":   # Se verifica si la elección del usuario es "dividir". Si es así, se calcula el monto que cada persona debe pagar dividiendo el total de la cuenta entre el número de personas.
            cuentaTotal = sum(costo for persona in pedidos.values() for plato, costo in persona)  # Se calcula el total de la cuenta sumando los costos de todos los pedidos.
            cuentaPorIndividuo = cuentaTotal / personas   # Se calcula el monto que cada persona debe pagar dividiendo el total de la cuenta entre el número de personas.
            print(f"Cada persona debe pagar: ${cuentaPorIndividuo:.2f}")  # Se muestra el monto que cada persona debe pagar sin propina por persona.
            print("Va a dejar propina?")   # Se solicita al usuario que ingrese si van a dejar propina o no.
            propina = input("Escribe 'si' para dejar propina o 'no' para no dejar propina: ")

            if propina.lower() == "si":   # Se verifica si la elección del usuario es "si". Si es así, se solicita al usuario que ingrese el porcentaje de propina que desean dejar y se almacena en la variable 'propina'.
                propina = float(input("Cuanto quieren dejar de propina? (Escribe el porcentaje sin el símbolo %): "))
                propina = propina / 100 # Se convierte el porcentaje de propina a un decimal dividiendo entre 100.
                cuentaConPropina = cuentaPorIndividuo + (cuentaPorIndividuo * propina)  # Se calcula el monto que cada persona debe pagar con propina sumando el monto sin propina y el monto de la propina (que se calcula multiplicando el monto sin propina por el porcentaje de propina).
                print(f"Cada persona debe pagar con propina: ${cuentaConPropina:.2f}")  # Se muestra el monto que cada persona debe pagar con propina por persona.

            break   # Se rompe el bucle para salir de la verificación de la elección del usuario.

        elif division.lower() == "individual":   # Se verifica si la elección del usuario es "individual". Si es así, se muestra el monto que cada persona debe pagar por su pedido individualmente.
            for persona, pedidos_persona in pedidos.items():
                total_persona = sum(costo for plato, costo in pedidos_persona)  # Se calcula el total de la cuenta para cada persona sumando los costos de sus pedidos.
                print(f"{persona} debe pagar: ${total_persona:.2f}")  # Se muestra el monto que cada persona debe pagar por su pedido individualmente.
                print("Va a dejar propina?")   # Se solicita al usuario que ingrese si van a dejar propina o no.
                propina = input("Escribe 'si' para dejar propina o 'no' para no dejar propina: ")

                if propina.lower() == "si":   # Se verifica si la elección del usuario es "si". Si es así, se solicita al usuario que ingrese el porcentaje de propina que desean dejar y se almacena en la variable 'propina'.
                    propina = float(input("Cuanto quieren dejar de propina? (Escribe el porcentaje sin el símbolo %): "))
                    
                    propina = propina / 100 # Se convierte el porcentaje de propina a un decimal dividiendo entre 100.
                    total_con_propina = total_persona + (total_persona * propina)  # Se calcula el monto que cada persona debe pagar con propina sumando el monto sin propina y el monto de la propina (que se calcula multiplicando el monto sin propina por el porcentaje de propina).
                    print(f"{persona} debe pagar con propina: ${total_con_propina:.2f}")  # Se muestra el monto que cada persona debe pagar con propina por persona.
                elif propina.lower() == "no":   # Se verifica si la elección del usuario es "no". Si es así, se muestra un mensaje indicando que no se dejará propina.
                    print(f"{persona} no dejó propina.")
                    print(f"{persona} debe pagar: ${total_persona:.2f}")  # Se muestra el monto que cada persona debe pagar sin propina por persona.
                else:   # Si la elección del usuario no es válida, se muestra un mensaje de error indicando que la opción ingresada no es válida.
                    print("Error: Opción no válida. Por favor, ingresa 'si' o 'no'.")  # Si la elección del usuario no es válida, se muestra un mensaje de error indicando que la opción ingresada no es válida.
            break   # Se rompe el bucle para salir de la verificación de la elección del usuario.
            
        else:   # Si la elección del usuario no es válida, se muestra un mensaje de error indicando que la opción ingresada no es válida.
            print("Error: Opción no válida. Por favor, ingresa 'dividir' o 'individual'.")




def iniciadorDeProgramas():   # Se define la función para iniciar el programa.

    print("------------------------------------")
    print("Bienvenido a tu programas de vida real")   # Se muestra un mensaje de bienvenida al programa.
    print("------------------------------------")

    print("Selecciona el programa que deseas ejecutar:")   # Se muestra un mensaje solicitando al usuario que seleccione el programa que desea ejecutar.

    print("1. Programa para calcular la cuenta en un restaurante.")   # Se muestra la opción 1 para calcular el pago de una cuenta en un restaurante, incluyendo la propina.

    print("2. Programa para ...")   # Se muestra la opción 2

    eleccion = input("Selecciona el programa que deseas ejecutar (Solo escribe el numero del programa): ")  # Se solicita al usuario que ingrese su elección de programa y se almacena en la variable 'eleccion'.


    if eleccion == "1":   # Se verifica si la elección del usuario es "1". Si es así, se llama a la función para calcular el pago de una cuenta en un restaurante.
        salidaAComer()

iniciadorDeProgramas()   # Se llama a la función para iniciar el programa.