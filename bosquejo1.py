import pprint

el_id = 0
compras = {}
total = 0


def menu():
    print("\n Elija una opción: ")
    print("    (1) cargar una compra")
    print("    (2) Eliminar compra")
    print("    (3) Listar compra")
    print("    (4) Modificar compra")
    print("    ó cualquier otra tecla para salir")
    global valor
    global eleccion
    eleccion = input()
    if eleccion == "1" or eleccion == "2" or eleccion == "3" or eleccion == "4":
        valor = True
        print("ingresada")
    else:
        valor = False
        print("Chau")


menu()


def alta(fecha, lugar, monto):
    global total
    global el_id

    total = total + float(monto)
    compras[el_id] = {"fecha": fecha, "lugar": lugar, "monto": monto}
    el_id += 1
    print("Nueva compra")


def borrar(id_borrar):
    global total
    global compras
    print(compras[id_borrar])

    total = total - (float(compras[id_borrar]["monto"]))
    del compras[id_borrar]
    print("Borrar compra")


def listar():
    global compras
    global total
    pprint.pprint(compras)
    print(total)
    print("Listar compras")


def modificar(compras, total, n):
    if n == 1:
        viejo = input("Ingrese el ID del evento que quiere modificar:  ")
        nuevo = str(input("Ingrese la nueva fecha:  "))
        compras[viejo]["fecha"] = nuevo

    elif n == 2:
        viejo = input("Ingrese el ID del evento que quiere modificar:  ")
        nuevo = str(input("Ingrese el nuevo lugar: "))
        compras[viejo]["lugar"] = nuevo

    elif n == 3:
        viejo = input("Ingrese el ID del evento que quiere modificar:  ")
        nuevo = float(input("Ingrese el nuevo monto:  "))
        total = total - compras[viejo]["monto"]
        compras[viejo]["monto"] = nuevo
        total = total + compras[viejo]["monto"]

    return compras, total


"""
def modificar(id_modificar, precio):
    global compras
    global total
    antes = float(compras[id_modificar]["monto"])
    compras[id_modificar]["monto"] = monto
    despues = float(compras[id_modificar]["monto"])
    total = total + despues - antes
"""

while valor == True:
    print("eleccion: ", eleccion)

    if eleccion == "1":
        fecha = input("ingrese la fecha: ")
        lugar = input("Ingrese el lugar: ")
        monto = input("ingrese el monto: ")
        alta(fecha, lugar, monto)
    elif eleccion == "2":
        id_borrar = input("Ingrese el id del elemento a borrar: ")
        borrar(int(id_borrar))
    elif eleccion == "3":
        listar()
    elif eleccion == "4":
        print("Que desea modificar:")
        print("   (1) La fecha")
        print("   (2) El lugar")
        print("   (3) El monto")
        n = int(input("elección: "))
        id_modificar = input("Ingrese el id de la operación: ").split()
        modificar(int(id_modificar), str(fecha), str(lugar), float(monto))
    else:
        break

    menu()
"""
for x in compras:
    # pprint.pprint("fecha: ", x[0], "lugar: ", x[1], "monto: ", x[2])
"""
# pprint.pprint(compras)
