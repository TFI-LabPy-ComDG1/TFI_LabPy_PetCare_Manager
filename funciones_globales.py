## Limpiador de Pantalla
def limpiar_pantalla():
    # Funciona en la mayoría de los casos sin importar el SO
    import os
    os.system("cls" if os.name == "nt" else "clear")

## Pausa y espera de enter
def pausar():
    input("\nPresione ENTER para continuar...")