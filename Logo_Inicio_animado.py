import time
import funciones_globales as FG
import msvcrt # Librería nativa de Windows para detectar teclas sin congelar el programa

def mostrar_logo_normal():
    print(r"  ██=============================================██  ")
    print(r"  ||                                             ||  ")
    print(r"  ||                                             ||  ")
    print(r"  ||                    /\_/\                    ||  ")
    print(r"  ||               ♥  =( °w° )=  ♥               ||  ")
    print(r"  ||                    )   (                    ||  ")
    print(r"  ||                   (__ __)                   ||  ")
    print(r"  ||             ╔═════════════════╗             ||  ")
    print(r"  ||             ║ PETCARE MANAGER ║             ||  ")
    print(r"  ||             ╚═════════════════╝             ||  ")
    print(r"  ||                                             ||  ")
    print(r"  ██=============================================██  ")
    print("\n          >> PRESIONE ENTER PARA INGRESAR <<         ")

def mostrar_logo_parpadeo():
    print(r"  ██=============================================██  ")
    print(r"  ||                                             ||  ")
    print(r"  ||                                             ||  ")
    print(r"  ||                    /\_/\                    ||  ")
    print(r"  ||               ♥  =( ^w^ )=  ♥               ||  ")
    print(r"  ||                    )   (                    ||  ")
    print(r"  ||                   (__ __)                   ||  ")
    print(r"  ||             ╔═════════════════╗             ||  ")
    print(r"  ||             ║ PETCARE MANAGER ║             ||  ")
    print(r"  ||             ╚═════════════════╝             ||  ")
    print(r"  ||                                             ||  ")
    print(r"  ██=============================================██  ")
    print("\n          >> PRESIONE ENTER PARA INGRESAR <<         ")

def esperar_con_deteccion(segundos):
    """
    Revisa cada 0.05 segundos si el usuario presionó Enter para
    salir inmediatamente sin trabar la animación.
    """
    pasos = int(segundos / 0.05)
    for _ in range(pasos):
        if msvcrt.kbhit():  # ¿El usuario presionó una tecla?
            tecla = msvcrt.getch()
            if tecla == b'\r':  # b'\r' es la tecla Enter en bytes
                return True     # Señal de que queremos salir
        time.sleep(0.05)
    return False

def logo_inicio_animado():
    while True:
        # 1. Mostrar logo normal
        FG.limpiar_pantalla()
        mostrar_logo_normal()
        
        # Espera 2 segundos (monitoreando si presionan Enter)
        if esperar_con_deteccion(2.0): 
            break

        # 2. Mostrar logo parpadeando
        FG.limpiar_pantalla()
        mostrar_logo_parpadeo()
        
        # Espera 0.2 segundos (monitoreando si presionan Enter)
        if esperar_con_deteccion(0.2): 
            break

    # Al salir del bucle limpia y continúa al programa principal
    FG.limpiar_pantalla()
    print(r"<< Vió parpadear al gatito?? >>")
    time.sleep(1.5)

# Ejecución de la pantalla de inicio animada
if __name__ == "__main__":
    logo_inicio_animado()