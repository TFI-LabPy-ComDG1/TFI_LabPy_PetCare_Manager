import Logo_Inicio as LG
import funciones_globales as FG

from menu_servicios import menu_servicios    
from menu_estadisticas import menu_estadisticas

def menu_principal():
    while True:
        FG.limpiar_pantalla()

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
                menu_Mascotas()
            case "2":
                menu_Turnos()
            case "3":
                menu_Atenciones()
            case "4": 
                menu_servicios()
            case "5":
                menu_estadisticas()
            case "0":
                print("\nHasta luego.")
                break
            case _:
                print("\nOpción inválida.")
                FG.pausar()

# Programa principal
LG.logo_inicio()
menu_principal()