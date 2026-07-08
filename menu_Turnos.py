import funciones_globales as FG

def menu_Turnos():
    hay_turno = False
    nombre_mascota = ""
    tipo_mascota = ""
    nombre_dueño = ""
    telefono = ""
    dia = ""
    hora = ""
    motivo = ""

    opcion = ""

    while opcion != "0":
        FG.limpiar_pantalla()

        print("|" , "=" * 38 , "|")
        print("|              MENU TURNOS               |")
        print("|" , "=" * 38 , "|")
        print("|                                        |")
        print("|  1. Registrar Turno                    |")
        print("|  2. Consultar Turnos                   |")
        print("|  3. Modificar Turno                    |")
        print("|  4. Cancelar Turno                     |")
        print("|                                        |")
        print("|  0. Volver al Menú Principal           |")
        print("|" , "=" * 38 , "|")
        print("")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            print("\n---- Registrar Turno --")

            nombre_mascota = input("Nombre de la mascota: ")
            while nombre_mascota == "":
                nombre_mascota = input("Ingrese el nombre de la mascota: ")

            tipo-mascota = input("Tipo de mascota: ")
            while tipo_mascota == "":
                tipo_mascota = input("Ingrese el tipo de mascota: ")

            nombre_dueño = input("Nombre del dueño: ")
            while nombre_dueño == "":
                nombre_dueño = input("Ingrese el nombre del dueño: ")

            telefono = input("Teléfono de contacto: ")
            motivo = input("Motivo de la consulta: ")

            print("\nDias disponibles")
            print("1. Lunes")
            print("2. Martes")
            print("3. Miércoles")
            print("4. Jueves")
            print("5. Viernes")

            dia_opcion = input("Seleccione el día: ")

            while dia_opcion != "1" and dia_opcion != "2" and dia_opcion != "3" and dia_opcion != "4" and dia_opcion != "5":
                dia_opcion = input("Seleccione un día válido (1-5): ")

            if dia_opcion == "1":
                dia = "Lunes"
            elif dia_opcion == "2":
                dia = "Martes"
            elif dia_opcion == "3":         
                dia = "Miércoles"
            elif dia_opcion == "4":
                dia = "Jueves"
            elif dia_opcion == "5":
                dia = "Viernes"

            print("\nHoras disponibles")
            print("1. 09:00")
            print("2. 10:00")
            print("3. 11:00")   
            print("4. 12:00")
            print("5. 17:00")
            print("6. 18:00")
            print("7. 19:00")

            hora_opcion = input("Seleccione la hora: ")

            while hora_opcion != "1" and hora_opcion != "2" and hora_opcion != "3" and hora_opcion != "4" and hora_opcion != "5" and hora_opcion != "6" and hora_opcion != "7":
                hora_opcion = input("Seleccione una hora válida (1-7): ")

            if hora_opcion == "1":
                hora = "09:00"
            elif hora_opcion == "2":
                hora = "10:00"
            elif hora_opcion == "3":
                hora = "11:00"
            elif hora_opcion == "4":
                hora = "12:00"
            elif hora_opcion == "5":
                hora = "17:00"
            elif hora_opcion == "6":
                hora = "18:00"
            elif hora_opcion == "7":
                hora = "19:00"  
            
            hay_turno = True
            print("\nEl turno ha sido registrado exitosamente.")
            FG.pausar()

        elif opcion == "2":
            print("\n---- Consultar Turnos ----")

            if hay_turno == True:
                print("\nTurno registrado:")
                print("Nombre de la mascota:", nombre_mascota)
                print("Tipo de mascota:", tipo_mascota)
                print("Nombre del dueño:", nombre_dueño)
                print("Teléfono de contacto:", telefono)
                print("Motivo de la consulta:", motivo)
                print("Día del turno:", dia)
                print("Hora del turno:", hora)
            else:
                print("\nNo hay turnos registrados.")

            FG.pausar()

        elif opcion == "3":
            print("\n---- Modificar Turno ----")

            if hay_turno == True:
                print ("1. modificar dia")
                print ("2. modificar hora")
                print ("3. modificar motivo")
                print ("4. modificar dia, hora y motivo")

                modificar = input("Seleccione la opción que desea modificar: ")

                while modificar != "1" and modificar != "2" and modificar != "3" and modificar != "4":
                    modificar = input("Seleccione una opción válida (1-4): ")

                if modificar == "1" or modificar == "4":
                    print("\nDias disponibles")
                    print("1. Lunes")
                    print("2. Martes")
                    print("3. Miércoles")
                    print("4. Jueves")
                    print("5. Viernes")

                    dia_opcion = input("Seleccione el día: ")

                    while dia_opcion != "1" and dia_opcion != "2" and dia_opcion != "3" and dia_opcion != "4" and dia_opcion != "5":
                        dia_opcion = input("Seleccione un día válido (1-5): ")

                    if dia_opcion == "1":
                        dia = "Lunes"
                    elif dia_opcion == "2":
                        dia = "Martes"
                    elif dia_opcion == "3":         
                        dia = "Miércoles"
                    elif dia_opcion == "4":
                        dia = "Jueves"
                    elif dia_opcion == "5":
                        dia = "Viernes"

                if modificar == "2" or modificar == "4":
                    print("\nHoras disponibles")
                    print("1. 09:00")
                    print("2. 10:00")
                    print("3. 11:00")   
                    print("4. 12:00")
                    print("5. 17:00")
                    print("6. 18:00")
                    print("7. 19:00")

                    hora_opcion = input("Seleccione la hora: ")

                    while hora_opcion != "1" and hora_opcion != "2" and hora_opcion != "3" and hora_opcion != "4" and hora_opcion != "5" and hora_opcion != "6" and hora_opcion != "7":
                        hora_opcion = input("Seleccione una hora válida (1-7): ")

                    if hora_opcion == "1":
                        hora = "09:00"
                    elif hora_opcion == "2":
                        hora = "10:00"
                    elif hora_opcion == "3":
                        hora = "11:00"
                    elif hora_opcion == "4":
                        hora = "12:00"
                    elif hora_opcion == "5":
                        hora = "17:00"
                    elif hora_opcion == "6":
                        hora = "18:00"
                    elif hora_opcion == "7":
                        hora = "19:00"
                
                if modificar == "3" or modificar == "4":
                    motivo = input("Motivo de la consulta: ")
                
                print("\nEl turno ha sido modificado exitosamente.")

            else:
                print("\nNo hay turnos registrados para modificar.")
            
            FG.pausar()

        elif opcion == "4":
            print("\n---- Cancelar Turno ----")

            if hay_turno == True:
                confirmar = input("¿Está seguro que desea cancelar el turno? (s/n): ")

                while confirmar != "s" and confirmar != "n":
                    confirmar = input("Ingrese 's' para sí o 'n' para no: ")

                if confirmar == "s":
                    hay_turno = False
                    nombre_mascota = ""
                    tipo_mascota = ""
                    nombre_dueño = ""
                    telefono = ""
                    dia = ""
                    hora = ""
                    motivo = ""

                    print("\nEl turno ha sido cancelado.")
                else:
                    print("\nEl turno no ha sido cancelado.")
                    
            else:
                 print("\nNo hay turnos registrados para cancelar.")
            FG.pausar ()

        elif opcion == "0":
            print("\nVolviendo al Menú Principal...")
            
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")
            FG.pausar()

    menu_Turnos() 

    