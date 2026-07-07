## IMPORTACIONES GLOBALES
import funciones_globales as FG
from Logo_Inicio_animado import logo_inicio_animado
from Logo_UTN import logo_UTN_animado

## IMPORTACIONES DE SUBMENUS
from menu_Mascotas import menu_Mascotas
from menu_Turnos import menu_Turnos
from menu_atenciones import menu_Atenciones
from menu_servicios import menu_servicios    
from menu_estadisticas import menu_estadisticas

## DESARROLLO DE MENU PRINCIPAL
def menu_principal():
    while True:
        FG.limpiar_pantalla()

        print("|" , "=" * 38 , "|")
        print("|        Sistema PetCare-Manager         |")
        print("|" , "=" * 38 , "|")
        print("|            Menu Principal              |")
        print("|  1. Mascotas                           |")
        print("|  2. Turnos                             |")
        print("|  3. Gestion Atenciones                 |")
        print("|  4. Gestion Servicios                  |")
        print("|  5. Estadísticas                       |")
        print("|  0. Salir                              |")
        print("|" , "=" * 38 , "|")
        print("")

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

# EJECUCION DE PROGRAMA
logo_UTN_animado()
logo_inicio_animado()
menu_principal()

