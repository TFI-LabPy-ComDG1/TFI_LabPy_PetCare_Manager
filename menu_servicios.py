import funciones_globales as FG

def menu_servicios():
    while True:
        FG.limpiar_pantalla()
        print("|", "=" * 38, "|")
        print("|        Gestión de Servicios            |")
        print("|", "=" * 38, "|")
        print("| 1. Agregar servicio                    |")
        print("| 2. Listar servicios                    |")
        print("| 0. Volver al Menú Principal            |")
        print("|", "=" * 38, "|")
        print("")
        
        opcion = input("Ingrese la opción deseada: ")
        
        match opcion:
            case "1":
                FG.limpiar_pantalla()
                print("|", "=" * 38, "|")
                print("|     --- Registrar Servicio ---         |")
                print("|", "=" * 38, "|")
                print("\n[Simulación] Ingrese nombre: Baño y Corte")
                print("[Simulación] Ingrese precio: $12000")
                print("\n-> ¡Servicio guardado con éxito!")
                FG.pausar()
            case "2":
                FG.limpiar_pantalla()
                print("|", "=" * 38, "|")
                print("|    --- Servicios Disponibles ---       |")
                print("|", "=" * 38, "|")
                print(" ID   | Detalle             | Precio")
                print("-" * 40)
                print(" 001  | Consulta Médica     | $8500")
                print(" 002  | Vacunación Quinta   | $11000")
                print(" 003  | Baño y Peluquería   | $12000")
                print(" 004  | Desparasitación     | $5000")
                print("-" * 40)
                FG.pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                FG.pausar()