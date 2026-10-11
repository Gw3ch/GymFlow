# Proyecto GymFlow
# Sistema para registrar y administrar máquinas de gimnasio
# Entrega final - Arreglos, funciones, ciclos y estructuras de decisión

# Arreglos para almacenar la información de las máquinas
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

names = [
    "Prensa de piernas",
    "Caminadora",
    "Peck Deck",
    "Press de pecho",
    "Extension de cuadriceps",
    "Curl femoral",
    "Jalon al pecho",
    "Remo sentado",
    "Maquina de hombros",
    "Bicicleta estatica"
]

areas = [
    "Piernas",
    "Cardio",
    "Pecho",
    "Pecho",
    "Piernas",
    "Piernas",
    "Espalda",
    "Espalda",
    "Hombros",
    "Cardio"
]

statuses = [
    "Ocupada",
    "Libre",
    "Mantenimiento",
    "Libre",
    "Ocupada",
    "Libre",
    "Ocupada",
    "Libre",
    "Mantenimiento",
    "Libre"
]

queues = [2, 0, 0, 0, 2, 0, 2, 0, 0, 0]

next_id = 11

# Arreglo bidimensional que agrupa los arreglos de información
machines = [ids, names, areas, statuses, queues]

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n===== GYMFLOW =====")
    print("1. Registrar máquina")
    print("2. Consultar máquinas")
    print("3. Modificar máquina")
    print("4. Eliminar máquina")
    print("5. Reservar / usar máquina")
    print("6. Salir")


# Menú principal
while True:
    mostrar_menu()

    option = input("Seleccione una opción: ")

    # Registrar máquina
    if option == "1":
        print("\n--- REGISTRAR MÁQUINA ---")

        name = input("Nombre de la máquina: ")
        area = input("Área del gimnasio: ")
        status = input(
            "Estado de la máquina (Libre/Ocupada/Mantenimiento): "
        ).capitalize()

        ids.append(next_id)
        names.append(name)
        areas.append(area)
        statuses.append(status)
        queues.append(0)

        next_id += 1

        print("Máquina registrada correctamente.")

    # Consultar máquinas
    elif option == "2":
        print("\n--- CONSULTAR MÁQUINAS ---")

        if len(ids) == 0:
            print("No hay máquinas registradas.")
        else:
            for i in range(len(ids)):
                print(
                    "ID:", ids[i],
                    "| Nombre:", names[i],
                    "| Área:", areas[i],
                    "| Estado:", statuses[i]
                )

    # Modificar máquina
    elif option == "3":
        print("\n--- MODIFICAR MÁQUINA ---")

        machine_id = input(
            "Digite el ID de la máquina que desea modificar: "
        )

        found = False

        for i in range(len(ids)):
            if str(ids[i]) == machine_id:
                names[i] = input("Nuevo nombre: ")
                areas[i] = input("Nueva área: ")
                statuses[i] = input(
                    "Nuevo estado (Libre/Ocupada/Mantenimiento): "
                ).capitalize()

                print("Máquina modificada correctamente.")
                found = True
                break

        if found == False:
            print("No se encontró una máquina con ese ID.")

    # Eliminar máquina
    elif option == "4":
        print("\n--- ELIMINAR MÁQUINA ---")

        machine_id = input(
            "Digite el ID de la máquina que desea eliminar: "
        )

        found = False

        for i in range(len(ids)):
            if str(ids[i]) == machine_id:
                ids.pop(i)
                names.pop(i)
                areas.pop(i)
                statuses.pop(i)
                queues.pop(i)

                print("Máquina eliminada correctamente.")
                found = True
                break

        if found == False:
            print("No se encontró una máquina con ese ID.")

    # Reservar / usar máquina
    elif option == "5":
        print("\n--- RESERVAR / USAR MÁQUINA ---")

        machine_id = input("Digite el ID de la máquina: ")

        found = False

        for i in range(len(ids)):
            if str(ids[i]) == machine_id:
                found = True

                print("Máquina:", names[i])
                print("Estado:", statuses[i])

                if statuses[i] == "Libre":
                    answer = input(
                        "¿Desea reservarla? (si/no): "
                    ).lower()

                    if answer == "si":
                        statuses[i] = "Ocupada"
                        print("Reserva realizada correctamente.")
                    else:
                        print("No se realizó la reserva.")

                elif statuses[i] == "Ocupada":
                    print("La máquina está ocupada.")
                    print("Personas en fila:", queues[i])

                    answer = input(
                        "¿Desea entrar a la fila? (si/no): "
                    ).lower()

                    if answer == "si":
                        queues[i] += 1
                        waiting_time = queues[i] * 15

                        print("Fue agregado a la fila.")
                        print("Su posición es:", queues[i])
                        print(
                            "Tiempo aproximado:",
                            waiting_time,
                            "minutos."
                        )
                    else:
                        print("No fue agregado a la fila.")

                elif statuses[i] == "Mantenimiento":
                    print("La máquina está en mantenimiento.")
                    print("No se puede utilizar.")

                else:
                    print("El estado de la máquina no es válido.")

                break

        if found == False:
            print("No se encontró una máquina con ese ID.")

    # Salir
    elif option == "6":
        print("Saliendo de GymFlow...")
        break

    else:
        print("Opción inválida.")
