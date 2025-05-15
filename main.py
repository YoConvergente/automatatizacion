from usuario import crear_usuario, listar_usuarios, modificar_usuario
from dispositivo import crear_dispositivo, listar_dispositivos, modificar_dispositivo
from automatizacion import crear_automatizacion, listar_automatizaciones, modificar_automatizacion

def crear_usuario_interactivo():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    rol = input("Rol (admin/invitado): ")
    usuario = crear_usuario(nombre, correo, rol)
    print(f"Usuario creado: {usuario}")

def menu():
    while True:
        print("""
==== SISTEMA DOMÓTICO ====
1. Crear usuario
2. Listar usuarios
3. Modificar usuario
4. Crear dispositivo
5. Listar dispositivos
6. Modificar dispositivo
7. Crear automatización
8. Listar automatizaciones
9. Modificar automatización
0. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_usuario_interactivo()
        elif opcion == "2":
            for u in listar_usuarios():
                print(u)
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            nombre = input("Nombre del dispositivo: ")
            tipo = input("Tipo: ")
            estado = input("Estado (ON/OFF): ")
            ubicacion = input("Ubicación: ")
            d = crear_dispositivo(nombre, tipo, estado, ubicacion)
            print(f"Dispositivo creado: {d}")
        elif opcion == "5":
            for d in listar_dispositivos():
                print(d)
        elif opcion == "6":
            modificar_dispositivo()
        elif opcion == "7":
            nombre = input("Nombre de automatización: ")
            condicion = input("Condición: ")
            accion = input("Acción: ")
            id_dispositivo = input("ID del dispositivo: ")
            id_usuario = input("ID del usuario: ")
            a = crear_automatizacion(nombre, condicion, accion, id_dispositivo, id_usuario)
            print(f"Automatización creada: {a}")
        elif opcion == "8":
            for a in listar_automatizaciones():
                print(a)
        elif opcion == "9":
            modificar_automatizacion()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

