### funciones
"""" definicion de una funcion
def nombre_de_la_funcion(parametro1, parametro2....)
# docstring
# cuerpo de la funcion
#
"""
def saludar():
    print("Hola")
    
def saludar_a(nombre):
    print(f"Hola... {nombre}")
saludar_a("Chicho")
saludar_a("Chapolina")
saludar_a("Lilo")
saludar_a("Ivett")

#EL PAREMETRO ES OBLIGATORIO
#EL ARGUMENTO ES OPCIONAL
def saludar_a_con_mensaje(nombre, mensaje="Bienvenido"):
    print(f"{mensaje}, {nombre}!")  
saludar_a_con_mensaje("Chicho")
saludar_a_con_mensaje("Chapolina", "Que gusto verte")
saludar_a_con_mensaje("Lilo", "Hola")   
