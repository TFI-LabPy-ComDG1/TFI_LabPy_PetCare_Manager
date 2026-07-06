import funciones_globales as FG

def menu_estadisticas():
    while True:
        FG.limpiar_pantalla()
        print("~" * 40)
        print("            Estadísticas")
        print("~" * 40)
        print("1. Servicios más frecuentes")
        print("2. Motivos de consulta más frecuentes")
        print("3. Mascotas más atendidas")
        print("0. Volver al Menú Principal")
        print("~" * 40)
        opcion = input("Ingrese la opción deseada: ")
        match opcion:
            case "1":
                FG.limpiar_pantalla()
                print("~" * 40)
                print(" --- Ranking de Servicios Solicitados ---")
                print("~" * 40)
                print("\n1. Consulta Médica Gral. (45 veces)")
                print("2. Baño y Peluquería     (32 veces)")
                print("3. Vacunación            (28 veces)")
                FG.pausar()
            case "2":
                FG.limpiar_pantalla()
                print("~" * 40)
                print("  --- Principales Motivos de Consulta ---")
                print("~" * 40)
                print("\n1. Control anual / Vacunas  (50%)")
                print("2. Problemas en la piel     (30%)")
                print("3. Accidentes / Urgencias   (20%)")
                FG.pausar()
            case "3":
                FG.limpiar_pantalla()
                print("~" * 40)
                print(" --- Mascotas con Más Atenciones ---")
                print("~" * 40)
                print("\n1. 'Thor' (Perro - Golden Retriever) -> 8 visitas")
                print("2. 'Luna' (Gato - Siamés)            -> 6 visitas")
                print("3. 'Rocco' (Perro - Caniche)         -> 5 visitas")
                FG.pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                FG.pausar()