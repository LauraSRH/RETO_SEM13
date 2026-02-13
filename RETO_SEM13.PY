#RETO SEMANA 13. Usando excepciones, try, else y finally, crear un programa que permita agregar 
# alumnos y sus calificaciones, mostrar la información de cada alumno y el promedio de sus calificaciones, y 
# salir del programa. El programa debe manejar errores de entrada de datos y permitir al usuario corregirlos
# Al iniciar se muestre un menú con las opciones:
# 1. Agregar un nuevo alumno.
# 2. Ver los alumnos y las calificaciones.
# 3. Salir.
# Si se decide agregar un nuevo alumno, corroborar que el nombre no esté en blanco.
# Preguntar cuántas calificaciones se quiere agregar.
# Si se ingresa una calificación que no sea de tipo numérico, se pedirá volver a intentar.
# Después de agregar la información de un alumno, volver al menú principal.
# Si se selecciona la opción 2, mostrar en la pantalla la información de cada alumno y 
# el promedio de sus calificaciones. Ejemplo: “Laura Ramírez: Promedio 9.5”
# Si se selecciona la opción ‘S’, indicar que se cerrará el programa y preguntar si se está
# seguro de cerrar el programa o no.
# No deberá detenerse la ejecución del programa en caso de ingresar valores equivocados.

alumnos = {} # diccionario para almacenar los alumnos y sus calificaciones
inicio = "Inicio del programa" #Muestra el inicio del programa y el menú para ingreso de datos.

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Agregar un nuevo alumno.")
    print("2. Ver los alumnos y promedio de sus calificaciones.")
    print("3. Salir.")
    return input("Seleccione una opción: ").strip()

def agregar_alumno(): #Función para agregar un nuevo alumno y sus calificaciones.
    """Ingreso de los datos del alumno, con manejo de excpeciones para validar la entrada de datos"""
    while True:
        nombre = input("Ingrese el nombre del alumno: ").strip() #Ingreso del nombre del alumno, con validación para que no esté en blanco.
        if nombre:
            break
        else:
            print("El nombre no puede estar en blanco. Por favor, intente de nuevo.")
    
    while True: #Ingreso de la cantidad de calificaciones, con manejo de excepciones para validar que sea un número entero y no negativo.
        try:
            num_calificaciones = int(input("¿Cuántas calificaciones desea agregar? "))
            if num_calificaciones < 0:
                print("El número de calificaciones no puede ser negativo. Por favor, intente de nuevo.")
                continue
            break
        except ValueError: #Si se ingresa un valor que no es un número entero, se mostrará un mensaje de error y se pedirá al usuario que intente de nuevo.
            print("Entrada inválida. Por favor, ingrese un número entero para las calificaciones.")
    
    calificaciones = [] #Ingreso de las calificaciones, con manejo de excepciones para validar que sean números 
    #y estén entre 0 y 10. Si se ingresa una calificación inválida, se mostrará un mensaje de error y se pedirá al usuario que intente de nuevo.
    for i in range(num_calificaciones):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
                if calificacion < 0 or calificacion > 10:
                    print("La calificación debe estar entre 0 y 10. Por favor, intente de nuevo.")
                    continue
                calificaciones.append(calificacion)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para la calificación.")
    
    alumnos[nombre] = calificaciones
    print(f"Alumno '{nombre}' agregado exitosamente con sus calificaciones.")

#Función para mostrar los alumnos y sus calificaciones, con manejo de excepciones para validar que 
# haya alumnos registrados antes de intentar mostrar la información.
def mostrar_alumnos():
    """Función para mostrar los alumnos y sus calificaciones, con manejo de excepciones 
    para validar que haya alumnos registrados antes de intentar mostrar la información."""
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    for nombre, calificaciones in alumnos.items():
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"{nombre}: Promedio {promedio:.2f}")

#Función para salir del programa, con confirmación del usuario, para evitar cierres accidentales.
def salir_programa():
    """Función para salir del programa, con confirmación del usuario."""
    while True:
        confirmacion = input("¿Está seguro de que desea salir del programa? (S/N): ").strip().upper()
        if confirmacion == 'S':
            print("Cerrando el programa. ¡Hasta luego!")
            return True
        elif confirmacion == 'N':
            print("Regresando al menú principal.")
            return False
        else:
            print("Entrada inválida. Por favor, ingrese 'S' para sí o 'N' para no.")

def main():
    print(inicio)
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            mostrar_alumnos()
        elif opcion == '3':
            if salir_programa():
                break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")
if __name__ == "__main__":    main()

