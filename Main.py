def limpiar_pantalla():
    # Funciona en la mayoría de los casos sin importar el SO
    import os
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione ENTER para continuar...")
    
def menu_servicios():
    while True:
        limpiar_pantalla()
        print("~" * 40)
        print("        Gestión de Servicios")
        print("~" * 40)
        print("1. Agregar servicio")
        print("2. Listar servicios")
        print("0. Volver al Menú Principal")
        print("~" * 40)
        opcion = input("Ingrese la opción deseada: ")
        match opcion:
            case "1":
                limpiar_pantalla()
                print("--- Registrar Nuevo Servicio ---")
                print("\n[Simulación] Ingrese nombre: Baño y Corte")
                print("[Simulación] Ingrese precio: $12000")
                print("\n-> ¡Servicio guardado con éxito (Simulado)!")
                pausar()
            case "2":
                limpiar_pantalla()
                print("--- Lista de Servicios Disponibles ---")
                print("-" * 40)
                print("ID   | Detalle             | Precio")
                print("-" * 40)
                print("001  | Consulta Médica     | $8500")
                print("002  | Vacunación Quinta   | $11000")
                print("003  | Baño y Peluquería   | $12000")
                print("004  | Desparasitación     | $5000")
                print("-" * 40)
                pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                pausar()

def menu_estadisticas():
    while True:
        limpiar_pantalla()
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
                limpiar_pantalla()
                print("--- Ranking de Servicios Más Solicitados ---")
                print("\n1. Consulta Médica Gral. (45 veces)")
                print("2. Baño y Peluquería     (32 veces)")
                print("3. Vacunación            (28 veces)")
                pausar()
            case "2":
                limpiar_pantalla()
                print("--- Principales Motivos de Consulta ---")
                print("\n1. Control anual / Vacunas  (50%)")
                print("2. Problemas en la piel     (30%)")
                print("3. Accidentes / Urgencias   (20%)")
                pausar()
            case "3":
                limpiar_pantalla()
                print("--- Mascotas con Mayor Cantidad de Atenciones ---")
                print("\n1. 'Thor' (Perro - Golden Retriever) -> 8 visitas")
                print("2. 'Luna' (Gato - Siamés)            -> 6 visitas")
                print("3. 'Rocco' (Perro - Caniche)         -> 5 visitas")
                pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                pausar()

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
                menu_servicios()
            case "5":
                menu_estadisticas()
            case "0":
                menu_()
            case _:
                print("\nOpción inválida.")
                pausar()

# Programa principal
menu_principal()
