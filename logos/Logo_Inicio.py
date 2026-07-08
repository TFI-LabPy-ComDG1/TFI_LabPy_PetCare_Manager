import utils.funciones_globales as FG

def logo_inicio():
    FG.limpiar_pantalla()
    print("  ██=============================================██  ")
    print("  ||                                             ||  ")
    print("  ||                                             ||  ")
    print("  ||                    /\_/\                    ||  ")
    print("  ||               ♥  =( °w° )=  ♥               ||  ")
    print("  ||                    )   (                    ||  ")
    print("  ||                   (__ __)                   ||  ")
    print("  ||             ╔═════════════════╗             ||  ")
    print("  ||             ║ PETCARE MANAGER ║             ||  ")
    print("  ||             ╚═════════════════╝             ||  ")
    print("  ||                                             ||  ")
    print("  ██=============================================██  ")
    FG.pausar()

if __name__ == "__main__":
    logo_inicio()

