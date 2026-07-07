import time
import funciones_globales as FG
import msvcrt # Librería nativa de Windows para detectar teclas sin congelar el programa

def Logo_UTN_arania():
    FG.limpiar_pantalla()
    print(r"  ██==============================================██  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░▄░░░░░▄▄░░░░░▄░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░▀█░░░░██░░░░█▀░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░▀█▄▄░██░▄▄█▀░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░█▄██▄█░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░██████████████░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░█▀██▀█░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░▄█▀▀░██░▀▀█▄░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░▄█░░░░██░░░░█▄░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░▀░░░░░▀▀░░░░░▀░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ██==============================================██  ")
    print("\n         >> PRESIONA ENTER PARA INGRESAR <<          ")

def Logo_UTN_nombre():
    FG.limpiar_pantalla()
    print(r"  ██==============================================██  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░╔╗░╔╦════╦═╗░╔╗░░░░╔═══╦═══╦═══╦═══╗░░░░░||  ")
    print(r"  ||░░░░░║║░║║╔╗╔╗║║╚╗║║░░░░║╔══╣╔═╗║╔═╗║╔══╝░░░░░||  ")
    print(r"  ||░░░░░║║░║╠╝║║╚╣╔╗╚╝║░░░░║╚══╣╚═╝║╚═╝║╚══╗░░░░░||  ")
    print(r"  ||░░░░░║║░║║░║║░║║╚╗║║╔══╗║╔══╣╔╗╔╣╔╗╔╣╔══╝░░░░░||  ")
    print(r"  ||░░░░░║╚═╝║░║║░║║░║║║╚══╝║║░░║║║╚╣║║╚╣╚══╗░░░░░||  ")
    print(r"  ||░░░░░╚═══╝░╚╝░╚╝░╚═╝░░░░╚╝░░╚╝╚═╩╝╚═╩═══╝░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||  ")
    print(r"  ██==============================================██  ")
    print("\n         >> PRESIONA ENTER PARA INGRESAR <<         ")

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

def logo_UTN_animado():
    while True:
        # 1. Mostrar logo normal
        FG.limpiar_pantalla()
        Logo_UTN_arania()
        
        # Espera 2 segundos (monitoreando si presionan Enter)
        if esperar_con_deteccion(1.0): 
            break

        # 2. Mostrar logo parpadeando
        FG.limpiar_pantalla()
        Logo_UTN_nombre()
        
        # Espera 0.2 segundos (monitoreando si presionan Enter)
        if esperar_con_deteccion(1.0): 
            break

    # Al salir del bucle limpia y continúa al programa principal
    FG.limpiar_pantalla()
    print(r"<< Agárrese a la silla profe... >>")
    time.sleep(1.5)

# Ejecución de la pantalla de inicio
#logo_UTN_animado()
