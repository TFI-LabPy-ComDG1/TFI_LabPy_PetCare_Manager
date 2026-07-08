import utils.funciones_globales as FG

def menu_estadisticas():
    while True:
        FG.limpiar_pantalla()
        print("|", "=" * 38, "|")
        print("|            Estadísticas                |")
        print("|", "=" * 38, "|")
        print("| 1. Servicios más frecuentes            |")
        print("| 2. Motivos de consulta frecuentes      |")
        print("| 3. Mascotas más atendidas              |")
        print("| 0. Volver al Menú Principal            |")
        print("|", "=" * 38, "|")
        print("")
        
        opcion = input("Ingrese la opción deseada: ")
        
        match opcion:
            case "1":
                FG.limpiar_pantalla()
                print("|", "=" * 38, "|")
                print("|   --- Ranking de Servicios ---         |")
                print("|", "=" * 38, "|")
                print("\n1. Consulta Médica Gral. (45 veces)")
                print("2. Baño y Peluquería     (32 veces)")
                print("3. Vacunación            (28 veces)")
                FG.pausar()
            case "2":
                FG.limpiar_pantalla()
                print("|", "=" * 38, "|")
                print("|    --- Motivos de Consulta ---         |")
                print("|", "=" * 38, "|")
                print("\n1. Control anual / Vacunas  (50%)")
                print("2. Problemas en la piel     (30%)")
                print("3. Accidentes / Urgencias   (20%)")
                FG.pausar()
            case "3":
                FG.limpiar_pantalla()
                print("|", "=" * 38, "|")
                print("|   --- Mascotas Más Atendidas ---       |")
                print("|", "=" * 38, "|")
                print("\n1. 'Thor' (Perro - Golden) -> 8 visitas")
                print("2. 'Luna' (Gato - Siamés)  -> 6 visitas")
                print("3. 'Rocco' (Perro - Caniche) -> 5 visitas")
                FG.pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                FG.pausar()

if __name__ == "__main__":
    menu_estadisticas()

