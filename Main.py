def limpiar_pantalla():
    # Funciona en la mayoría de los casos sin importar el SO
    import os
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione ENTER para continuar...")

def menu_principal():
    while True:
        limpiar_pantalla()

        print("~" * 40)
        print("    Sistema PetCare-Manager")
        print("~" * 40)
        print("  - Menu Principal - ")
        print("1. Mascotas")
        print("2. Turnos")
        print("3. Gestion Atenciones")
        print("4. Gestion Servicios")
        print("5. Estadísticas")
        print("0. Salir")
        print("~" * 40)

        opcion = input("Ingrese la opcion deseada:")

        match opcion:
            case "1":
                menu_()
            case "2":
                menu_()
            case "3":
                menu_()
            case "4":
                menu_()
            case "5":
                menu_()
            case "0":
                menu_()
            case _:
                print("\nOpción inválida.")
                pausar()

# Programa principal
menu_principal()
