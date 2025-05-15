usuarios = []
contador_usuarios = 0

def generar_id_usuario(nombre):
    global contador_usuarios
    contador_usuarios += 1
    return f"{nombre.lower()}_{contador_usuarios}"

def crear_usuario(nombre, correo, rol):
    id_usuario = generar_id_usuario(nombre)
    usuario = {
        "id_usuario": id_usuario,
        "nombre": nombre,
        "correo": correo,
        "rol": rol
    }
    usuarios.append(usuario)
    return usuario

def listar_usuarios():
    return usuarios

def buscar_usuario(id_usuario):
    for u in usuarios:
        if u["id_usuario"] == id_usuario:
            return u
    return None

def modificar_usuario():
    id_usuario = input("Ingrese el ID del usuario a modificar: ")
    usuario = buscar_usuario(id_usuario)
    if usuario:
        usuario["nombre"] = input("Nuevo nombre: ")
        usuario["correo"] = input("Nuevo correo: ")
        usuario["rol"] = input("Nuevo rol: ")
        print("Usuario modificado.")
    else:
        print("Usuario no encontrado.")

