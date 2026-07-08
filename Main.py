## IMPORTACIONES GLOBALES
import utils.funciones_globales as FG
from logos.Logo_Inicio_animado import logo_inicio_animado
from logos.Logo_UTN import logo_UTN_animado
from logos.logo_fin import Logo_UTN_fin

## IMPORTACIONES DE SUBMENUS
from menus.menu_Mascotas import menu_Mascotas
from menus.menu_Turnos import menu_Turnos
from menus.menu_atenciones import menu_Atenciones
from menus.menu_servicios import menu_servicios    
from menus.menu_estadisticas import menu_estadisticas

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
def main():
    logo_UTN_animado()
    logo_inicio_animado()
    menu_principal()
    Logo_UTN_fin()

if __name__ == "__main__":
    main()

