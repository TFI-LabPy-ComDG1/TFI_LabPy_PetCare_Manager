import utils.funciones_globales as FG

def menu_Atenciones():
    while True:
        FG.limpiar_pantalla()
        print("|" , "=" * 38 , "|")
        print("|            Menu Atenciones             |")
        print("|" , "=" * 38 , "|")
        print("|                                        |")
        print("|  1. Registrar atención                 |")
        print("|  2. Listar atenciones                  |")
        print("|  0. Volver al Menú Principal           |")
        print("|" , "=" * 38 , "|")
        print("")

        opcion = input("Ingrese la opción deseada:")

        match opcion:
            case "1":
                FG.limpiar_pantalla()
                print("| ===================================== |")
                print("|          Registrar atención           |")
                print("| ======================================|")
                print("\nTurnos pendientes:")
                print(" ID   | Fecha y hora             | Motivo  | Mascota")
                print(" 001  | 20/04/2026 18:00         | Vómitos | Filurais")
                print("\n[Simulación] Ingrese el ID de la atención disponible: 1")
                print("[Simulación] Ingrese el diagnóstico: Gastroenteritis aguda")
                print("\nServicios disponibles")
                print(" ID   | Detalle             | Precio")
                print("-" * 40)
                print(" 001  | Consulta Médica     | $8500")
                print(" 002  | Vacunación Quinta   | $11000")
                print(" 003  | Baño y Peluquería   | $12000")
                print(" 004  | Desparasitación     | $5000")
                print("-" * 40)
                print("\n[Simulación] Ingrese el ID del servicio a realizar: 2")
                print("\n-> ¡Atención registrada con éxito!")
                FG.pausar()
            case "2":
                FG.limpiar_pantalla()
                print("| ===================================== |")
                print("|           Listar atenciones           |")
                print("| ======================================|")
                print(" ID   | Diagnóstico             | Costo  | Mascota     | Servicio")
                print(" 001  | Gastroenteritis aguda   | $11000 | Filurais    | Vacunación Quinta")
                FG.pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                FG.pausar()

if __name__ == "__main__":
    menu_Atenciones()

