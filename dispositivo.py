dispositivos = []
contador_dispositivos = 0

def generar_id_dispositivo():
    global contador_dispositivos
    contador_dispositivos += 1
    return f"disp_{contador_dispositivos}"

def crear_dispositivo(nombre, tipo, estado, ubicacion):
    id_dispositivo = generar_id_dispositivo()
    dispositivo = {
        "id_dispositivo": id_dispositivo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "ubicacion": ubicacion
    }
    dispositivos.append(dispositivo)
    return dispositivo

def listar_dispositivos():
    return dispositivos

def buscar_dispositivo(id_dispositivo):
    for d in dispositivos:
        if d["id_dispositivo"] == id_dispositivo:
            return d
    return None

def modificar_dispositivo():
    id_dispositivo = input("Ingrese el ID del dispositivo a modificar: ")
    dispositivo = buscar_dispositivo(id_dispositivo)
    if dispositivo:
        dispositivo["nombre"] = input("Nuevo nombre: ")
        dispositivo["tipo"] = input("Nuevo tipo: ")
        dispositivo["estado"] = input("Nuevo estado (ON/OFF): ")
        dispositivo["ubicacion"] = input("Nueva ubicación: ")
        print("Dispositivo modificado.")
    else:
        print("Dispositivo no encontrado.")

