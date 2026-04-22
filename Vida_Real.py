# Programa con problemas de la vida real

# Joan Mauricio Gutérrez Abril
def salidaAComer():     #Se define la función para calcular el pago de una cuenta en un restaurante, incluyendo la propina.

    print("=====================================")
    print("Hora de pagar la cuenta")        # Se muestra un mensaje indicando que es hora de pagar la cuenta.
    print("=====================================")

    pedidos = {}
    personas = int(input("Cuantas personas salieron a comer? "))    # Se solicita al usuario que ingrese el número de personas que salieron a comer y se almacena en la variable 'personas'.

    for i in range(personas):   # Se utiliza un bucle for para solicitar al usuario que ingrese el nombre y el precio de cada pedido. El bucle se ejecuta 3 veces, permitiendo ingresar 3 pedidos.
        nombre = input(f"Ingresa el nombre de la persona {i+1}: ")   # Se solicita al usuario que ingrese el nombre de la persona y se almacena en la variable 'nombre'.
        pedidos[nombre] = []  # Se solicita al usuario que ingrese el precio del pedido de la persona y se almacena en el diccionario 'pedidos' con el nombre como clave y el precio como valor.

        while True:    # Se utiliza un bucle while para permitir al usuario ingresar múltiples precios para cada persona. El bucle se ejecuta hasta que el usuario ingresa "fin".
            plato = input(f"¿Qué pidió {nombre}? ")
            pedidos[nombre].append(plato)
            
            continuar = input("¿Agregar otro plato? (si/no): ")
            if continuar.lower() != "si":
                break






    #personas = int(input("Cuantas personas salieron a comer? "))    # Se solicita al usuario que ingrese el número de personas que salieron a comer y se convierte a un entero.

    for persona, comida in pedidos.items():
    print(f"{persona} pidió: {', '.join(comida)}")

    cuentaTotal = float(input("Cual fue el total de la cuenta? "))  # Se solicita al usuario que ingrese el total de la cuenta y se convierte a un número flotante.

    cuentaIndividual = cuentaTotal / personas   # Se calcula el monto que cada persona debe pagar dividiendo el total de la cuenta entre el número de personas.


    if cuentaIndividual < 0:    # Se verifica si el resultado es un número negativo. Si es así, se muestra un mensaje de error indicando que el total de la cuenta no puede ser negativo.
        print("Error: El total de la cuenta no puede ser negativo.")

    elif not isinstance(cuentaIndividual, (int, float)):    # Se verifica si el resultado no es un número. Si es así, se muestra un mensaje de error indicando que el total de la cuenta debe ser un número.
        print("Error: El total de la cuenta debe ser un número.")

    else:       # Si el resultado es un número válido, se redondea a dos decimales y se muestra el monto que cada persona debe pagar sin propina.
            if isinstance(cuentaIndividual, float): # Se verifica si el resultado es un número flotante. Si es así, se redondea y se convierte a un entero.
                cuentaIndividual = round(cuentaIndividual, 0)
                cuentaIndividual = int(cuentaIndividual)
    propina = float(input("Cuanto quieren dejar de propina? (Escribe el porcentaje sin el símbolo %): "))   # Se solicita al usuario que ingrese el porcentaje de propina que desean dejar y se convierte a un número flotante.


    if propina < 0: # Se verifica si el porcentaje de propina es negativo. Si es así, se muestra un mensaje de error indicando que la propina no puede ser negativa.
        print("Error: La propina no puede ser negativa.")
    elif not isinstance(propina, (int, float)): # Se verifica si el porcentaje de propina no es un número. Si es así, se muestra un mensaje de error indicando que la propina debe ser un número.
        print("Error: La propina debe ser un número.")
    else:   # Si el porcentaje de propina es un número válido, se convierte a un decimal dividiendo entre 100 y se muestra el monto que cada persona debe pagar con propina.


        propina = propina / 100 # Se convierte el porcentaje de propina a un decimal dividiendo entre 100.

        propina = round(propina, 0) # Se redondea el porcentaje de propina.


    print(f"Cada persona debe pagar sin propina: ${cuentaIndividual}")  # Se muestra el monto que cada persona debe pagar sin propina por persona.
    cuentaConPropina = cuentaIndividual + (cuentaIndividual * propina)  # Se calcula el monto que cada persona debe pagar con propina sumando el monto sin propina y el monto de la propina (que se calcula multiplicando el monto sin propina por el porcentaje de propina).
    print(f"Cada persona debe pagar con propina: ${cuentaConPropina}")  # Se muestra el monto que cada persona debe pagar con propina por persona.





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