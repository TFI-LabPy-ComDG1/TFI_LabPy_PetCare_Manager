import utils.funciones_globales as FG

def menu_Mascotas():
    while True:
        FG.limpiar_pantalla()
        print("|" , "=" * 38 , "|")
        print("|             Menu Mascotas              |")
        print("|" , "=" * 38 , "|")
        print("|                                        |")
        print("|  1. Registrar mascota                  |")
        print("|  2. Listar mascotas                    |")
        print("|  3. Buscar mascota                     |")
        print("|  4. Eliminar mascota                   |")
        print("|  0. Volver al Menú Principal           |")
        print("|" , "=" * 38 , "|")
        print("")

        opcion = input("Ingrese la opción deseada:")

        match opcion:
            case "1":
                FG.limpiar_pantalla()
                print("| ===================================== |")
                print("|         Registrar mascota             |")
                print("| ======================================|")
                print("\n[Simulación] Ingrese el nombre de la mascota: Filurais")
                print("[Simulación] Ingrese la especie: Perro")
                print("[Simulación] Ingrese la raza: Caniche")
                print("[Simulación] Ingrese la edad (años): 5")
                print("[Simulación] Ingrese el nombre del dueño: Fulano")
                print("[Simulación] Ingrese el número de teléfono de contacto: 547-483")
                print("\n -> ¡Mascota registrada con éxito!")
                FG.pausar()
            case "2":
                FG.limpiar_pantalla()
                print("| ===================================== |")
                print("|         Listado de mascotas           |")
                print("| ======================================|")
                print(" ID   | Nombre             | Especie  | Raza     | Edad | Dueño         | Teléfono")
                print(" 001  | Filurais           | Perro    | Caniche  | 5    | Fulano        | 547-483 ")
                print(" 002  | Max                | Perro    | Labrador | 5    | Ana Pérez     | 555-1234")
                print(" 003  | Bella              | Gato     | Siames   | 3    | Carlos López  | 555-5678")
                FG.pausar()
            case "3":
                FG.limpiar_pantalla()
                print("| ===================================== |")
                print("|           Buscar mascota              |")
                print("| ======================================|")
                print("\n[Simulación] Ingrese el nombre de la mascota o del dueño: Carlos López")
                print("\n 003  | Bella              | Gato     | Siames   | 3    | Carlos López  | 555-5678")
                FG.pausar()
            case "4":
                FG.limpiar_pantalla()
                print("| ===================================== |")
                print("|           Eliminar mascota            |")
                print("| ======================================|")
                print(" ID   | Nombre             | Especie  | Raza     | Edad | Dueño         | Teléfono")
                print(" 001  | Filurais           | Perro    | Caniche  | 5    | Fulano        | 547-483 ")
                print(" 002  | Max                | Perro    | Labrador | 5    | Ana Pérez     | 555-1234")
                print(" 003  | Bella              | Gato     | Siames   | 3    | Carlos López  | 555-5678")
                print("\n[Simulación] Ingrese el ID de la mascota: 2")
                print("\n -> Mascota Max eliminado con éxito")
                FG.pausar()
            case "0":
                break
            case _:
                print("\nOpción inválida.")
                FG.pausar()

if __name__ == "__main__":
    menu_Mascotas()

