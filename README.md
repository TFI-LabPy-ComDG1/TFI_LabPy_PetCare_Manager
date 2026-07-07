```text
██==============================================██
||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░▄░░░░░▄▄░░░░░▄░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░▀█░░░░██░░░░█▀░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░▀█▄▄░██░▄▄█▀░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░░░░█▄██▄█░░░░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░██████████████░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░░░░█▀██▀█░░░░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░▄█▀▀░██░▀▀█▄░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░▄█░░░░██░░░░█▄░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░▀░░░░░▀▀░░░░░▀░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||
||░░░░░╔╗░╔╦════╦═╗░╔╗░░░░╔═══╦═══╦═══╦═══╗░░░░░||
||░░░░░║║░║║╔╗╔╗║║╚╗║║░░░░║╔══╣╔═╗║╔═╗║╔══╝░░░░░||
||░░░░░║║░║╠╝║║╚╣╔╗╚╝║░░░░║╚══╣╚═╝║╚═╝║╚══╗░░░░░||
||░░░░░║║░║║░║║░║║╚╗║║╔══╗║╔══╣╔╗╔╣╔╗╔╣╔══╝░░░░░||
||░░░░░║╚═╝║░║║░║║░║║║╚══╝║║░░║║║╚╣║║╚╣╚══╗░░░░░||
||░░░░░╚═══╝░╚╝░╚╝░╚═╝░░░░╚╝░░╚╝╚═╩╝╚═╩═══╝░░░░░||
||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||
||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░||
██==============================================██
```


# 🐾 PetCare Manager

PetCare Manager es un sistema de administración para veterinarias orientado a pequeños y medianos establecimientos, desarrollado como Trabajo Final Integrador de la cátedra Algoritmos y Estructuras de Datos.

---

## 📖 Descripción


Este proyecto consiste en el desarrollo de un sistema de gestión para una veterinaria urbana, especializada en la atención de mascotas domésticas convencionales. La aplicación fue desarrollada en Python y tiene como objetivo facilitar la administración de las actividades habituales del establecimiento.

El sistema permitirá gestionar el registro de mascotas, la asignación de turnos, la atención médica y el control de los servicios realizados. Además, incorporará estadísticas básicas relacionadas con los tipos de consultas y los servicios más frecuentes, con el fin de brindar información útil para la gestión del negocio.

Como alcance del proyecto, se definió que la aplicación será utilizada exclusivamente por el personal administrativo de la veterinaria. Por este motivo, no se implementarán mecanismos de autenticación, gestión de usuarios ni control de permisos.

La aplicación se ejecutará íntegramente desde la consola y estará organizada de forma modular. Su funcionamiento se estructurará mediante un menú principal y distintos submenús, cada uno correspondiente a un área funcional del sistema.

Permite gestionar la información de:

- 🐶 Mascotas
- 👤 Clientes
- 🩺 Veterinarios
- 📅 Turnos
- 💉 Historial clínico
- 💰 Facturación

---

## 👨‍💻 Tecnologías

- Python 3
- Programación modular
- Estructuras condicionales y repetitivas 
- Menús por consola
- IAs aplicadas en:
  - Equivalencias de estructuras en pseudocodigo a python.
  - Funciones especiales de phython con sus librerias.

---

## 📂 Estructura

```text
PetCare_Manager/
│
├── 📄 main.py                     # Punto de entrada del programa
├── 📄 README.md
├── 📄 LICENSE
│
├── 📁 menus/                      # Menús y navegación
│   ├── menu_mascotas.py
│   ├── menu_turnos.py
│   ├── menu_atenciones.py
│   ├── menu_servicios.py
│   └── menu_estadisticas.py
│
├── 📁 utils/                      # Funciones auxiliares
│   └── funciones_globales.py
│
├── 📁 logos/                      # Animaciones y arte ASCII
│   ├── logo_inicio.py
│   └── logo_utn.py
│
├── 📁 datos/                      # Archivos de persistencia
│   └── ...
│
└── 📁 docs/                       # Documentación e imágenes
```

---

## 🎓 Información académica

**Materia**

Algoritmos y Estructuras de Datos

**Trabajo**

Trabajo Final Integrador - Tema 14: Gestion de Veterinaria

**Año**

2026

**Universidad**

Universidad Tecnológica Nacional  
Facultad Regional Resistencia

---

## 👥 Grupo 1 - Comision D 2026

 - Burgos Kaenel, Guido Martin
 - Casarrubia, Aldo
 - Casarrubia, Lisandro
 - Marin Sosa, Jose Manuel
 - Pastori, Jose María

---

## 📄 Licencia

GPL-3.0
