automatizaciones = []
contador_automatizaciones = 0

def generar_id_automatizacion():
    global contador_automatizaciones
    contador_automatizaciones += 1
    return f"auto_{contador_automatizaciones}"

def crear_automatizacion(nombre, condicion, accion, id_dispositivo, id_usuario):
    id_automatizacion = generar_id_automatizacion()
    automatizacion = {
        "id_automatizacion": id_automatizacion,
        "nombre": nombre,
        "condicion": condicion,
        "accion": accion,
        "id_dispositivo": id_dispositivo,
        "id_usuario": id_usuario
    }
    automatizaciones.append(automatizacion)
    return automatizacion

def listar_automatizaciones():
    return automatizaciones

def buscar_automatizacion(id_automatizacion):
    for a in automatizaciones:
        if a["id_automatizacion"] == id_automatizacion:
            return a
    return None

def modificar_automatizacion():
    id_automatizacion = input("Ingrese ID de automatización: ")
    automatizacion = buscar_automatizacion(id_automatizacion)
    if automatizacion:
        automatizacion["nombre"] = input("Nuevo nombre: ")
        automatizacion["condicion"] = input("Nueva condición: ")
        automatizacion["accion"] = input("Nueva acción: ")
        automatizacion["id_dispositivo"] = input("Nuevo ID dispositivo: ")
        automatizacion["id_usuario"] = input("Nuevo ID usuario: ")
        print("Automatización modificada.")
    else:
        print("Automatización no encontrada.")

