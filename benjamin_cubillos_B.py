letras = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
numeros = "1234567890"

compras = []

def comprobar_nombre(mensaje):
    while True:
        try:
            nombre = input(mensaje).strip().capitalize()
            if compras == []:
                return nombre
            elif any(i["nombre"] == nombre for i in compras):
                raise ValueError("Ese comprador ya existe!")
            else:
                return nombre
        except ValueError as e:
            print(e)
            continue

def comprobar_entrada(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip().upper()
            if entrada not in "GV":
                raise ValueError("Tipo de entrada invalida!")
            else:
                return entrada
        except ValueError as e:
            print(e)
            continue

def comprobar_codigo(mensaje, letras, numeros):
    while True:
        try:
            codigo = input(mensaje).strip()
            if len(codigo) < 6:
                raise ValueError("Código no válido. Intente otra vez.")
            comprobacion_letras = any(i in letras for i in codigo)
            comprobacion_numeros = any(i in numeros for i in codigo)
            comprobacion_espacio = any(i == " " for i in codigo)
            if comprobacion_letras and comprobacion_numeros and not comprobacion_espacio:
                print("Código validado. ¡Entrada registrada con éxito!")
                return codigo
            else:
                raise ValueError("Código no válido. Intente otra vez.")
        except ValueError as e:
            print(e)
            continue

def comprar_entrada():
    nombre = comprobar_nombre("Ingrese nombre del comprador: ")
    entrada = comprobar_entrada("Ingrese tipo de entrada (G/V): ")
    codigo = comprobar_codigo("Ingrese código de confirmación: ", letras, numeros)

    compras.append({
        "nombre": nombre,
        "entrada": entrada,
        "codigo": codigo
    })

def consultar_comprador():
    while True:
        try:
            if compras == []:
                raise ValueError("No existen compras!")
            else:
                nombre = input("Ingrese nombre del comprador a buscar: ").strip().capitalize()
                for i in compras:
                    if i["nombre"] == nombre:
                        print(f"Tipo de entrada: {i["entrada"]}, Código: {i["codigo"]}")
                        break
                else:
                    raise ValueError("El comprador no se encuentra.")
                break
        except ValueError as e:
            print(e)
            break

def cancelar_compra():
    while True:
        try:
            if compras == []:
                raise ValueError("No existen compras!")
            else:
                nombre = input("Ingrese nombre del comprador a cancelar: ").strip().capitalize()
                for i in compras:
                    if i["nombre"] == nombre:
                        print("¡Compra cancelada!")
                        compras.remove(i)
                        break
                else:
                    raise ValueError("No se pudo cancelar la compra.")
                break
        except ValueError as e:
            print(e)
            break

def menu():
    while True:
        try:
            print("MENU PRINCIPAL")
            print("1.- Comprar entrada.")
            print("2.- Consultar comprador.")
            print("3.- Cancelar compra.")
            print("4.- Salir.")

            opcion = int(input("Ingrese una opción(1-4): "))

            if opcion == 1:
                comprar_entrada()
            elif opcion == 2:
                consultar_comprador()
            elif opcion == 3:
                cancelar_compra()
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("Debe ingresar una opción válida!!")
            continue

menu()