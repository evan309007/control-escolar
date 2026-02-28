Sistema de Control Escolar - CRUD
Operaciones:
1. Crear estudiante
2. Listar estudiantes
3. Consultar por ID
4. Actualizar estudiante
5. Eliminar estudiante

Persistencia mediante archivo JSON.
"""

import json
from pathlib import Path

DB_PATH = Path("estudiantes.json")


# --------------------------------
# Capa de Datos (Persistencia)
# --------------------------------
def cargar_estudiantes():
    if not DB_PATH.exists():
        return []

    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def guardar_estudiantes(estudiantes):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, indent=2, ensure_ascii=False)


# --------------------------------
# Funciones auxiliares
# --------------------------------
def generar_id(estudiantes):
    if not estudiantes:
        return 1
    return max(e["id"] for e in estudiantes) + 1


def buscar_por_id(estudiantes, estudiante_id):
    for e in estudiantes:
        if e["id"] == estudiante_id:
            return e
    return None


# --------------------------------
# Operaciones CRUD
# --------------------------------
def crear_estudiante(estudiantes):

    print("\nCrear estudiante")

    nombre = input("Nombre: ").strip()
    carrera = input("Carrera: ").strip()
    semestre = int(input("Semestre: "))

    nuevo = {
        "id": generar_id(estudiantes),
        "nombre": nombre,
        "carrera": carrera,
        "semestre": semestre
    }

    estudiantes.append(nuevo)
    guardar_estudiantes(estudiantes)

    print("Estudiante creado correctamente.")


def listar_estudiantes(estudiantes):

    print("\nLista de estudiantes")

    if not estudiantes:
        print("No existen registros.")
        return

    for e in estudiantes:
        print(f"ID:{e['id']} | {e['nombre']} | {e['carrera']} | Sem:{e['semestre']}")


def consultar_estudiante(estudiantes):

    print("\nConsultar estudiante")

    estudiante_id = int(input("ID del estudiante: "))

    e = buscar_por_id(estudiantes, estudiante_id)

    if e:
        print(e)
    else:
        print("Estudiante no encontrado.")


def actualizar_estudiante(estudiantes):

    print("\nActualizar estudiante")

    estudiante_id = int(input("ID del estudiante: "))
    e = buscar_por_id(estudiantes, estudiante_id)

    if not e:
        print("Estudiante no encontrado.")
        return

    nombre = input("Nuevo nombre (Enter para mantener): ").strip()
    carrera = input("Nueva carrera (Enter para mantener): ").strip()
    semestre_txt = input("Nuevo semestre (Enter para mantener): ").strip()

    if nombre:
        e["nombre"] = nombre

    if carrera:
        e["carrera"] = carrera

    if semestre_txt:
        e["semestre"] = int(semestre_txt)

    guardar_estudiantes(estudiantes)

    print("Estudiante actualizado.")


def eliminar_estudiante(estudiantes):

    print("\nEliminar estudiante")

    estudiante_id = int(input("ID del estudiante: "))
    e = buscar_por_id(estudiantes, estudiante_id)

    if not e:
        print("Estudiante no encontrado.")
        return

    estudiantes.remove(e)
    guardar_estudiantes(estudiantes)

    print("Estudiante eliminado.")


# --------------------------------
# Interfaz de Usuario (Menú)
# --------------------------------
def menu():

    estudiantes = cargar_estudiantes()

    while True:

        print("\nSistema de Control Escolar")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Consultar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_estudiante(estudiantes)

        elif opcion == "2":
            listar_estudiantes(estudiantes)

        elif opcion == "3":
            consultar_estudiante(estudiantes)

        elif opcion == "4":
            actualizar_estudiante(estudiantes)

        elif opcion == "5":
            eliminar_estudiante(estudiantes)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


if _name_ == "_main_":
    menu()
