# RETO SEMANA 13
Criterios del programa
Usando excepciones, try, else y finally, crear un programa que permita agregar 
alumnos y sus calificaciones, mostrar la información de cada alumno y el promedio de sus calificaciones, y 
salir del programa. El programa debe manejar errores de entrada de datos y permitir al usuario corregirlos
Al iniciar se muestre un menú con las opciones:
1. Agregar un nuevo alumno.
2. Ver los alumnos y las calificaciones.
3. Salir.
Si se decide agregar un nuevo alumno, corroborar que el nombre no esté en blanco.
# Preguntar cuántas calificaciones se quiere agregar.
# Si se ingresa una calificación que no sea de tipo numérico, se pedirá volver a intentar.
# Después de agregar la información de un alumno, volver al menú principal.
# Si se selecciona la opción 2, mostrar en la pantalla la información de cada alumno y 
# el promedio de sus calificaciones. Ejemplo: “Laura Ramírez: Promedio 9.5”
# Si se selecciona la opción ‘S’, indicar que se cerrará el programa y preguntar si se está
# seguro de cerrar el programa o no.
# No deberá detenerse la ejecución del programa en caso de ingresar valores equivocados.

diccionario para almacenar los alumnos y sus calificaciones
Muestra el inicio del programa y el menú para ingreso de datos.

Función para agregar un nuevo alumno y sus calificaciones.
    """Ingreso de los datos del alumno, con manejo de excpeciones para validar la entrada de datos"""
Con while True ingreso del nombre del alumno, con validación para que no esté en blanco y con else indicando que el nombre no debe quedar en blanco.
Adem+as ingreso de la cantidad de calificaciones, con manejo de excepciones para validar que sea un número entero y no negativo.
Si se ingresa un valor que no es un número entero, se mostrará un mensaje de error y se pedirá al usuario que intente de nuevo.
Ingreso de las calificaciones, con manejo de excepciones para validar que sean números 
y estén entre 0 y 10. Si se ingresa una calificación inválida, se mostrará un mensaje de error y se pedirá al usuario que intente de nuevo.
Un ciclo for para ingresar las calificaciones del alumno.

Función para mostrar los alumnos y sus calificaciones, con manejo de excepciones para validar que 
haya alumnos registrados antes de intentar mostrar la información.
    """Función para mostrar los alumnos y sus calificaciones, con manejo de excepciones 
    para validar que haya alumnos registrados antes de intentar mostrar la información."""

Función para salir del programa, con confirmación del usuario, para evitar cierres accidentales.
  """Función para salir del programa, con confirmación del usuario."""

Este programa fue más complejo que el ejercicio anterior parecido al ingreso de alumnos y calificaciones. Igualmente, recibi apoyo de la guía de VSCode para poder terminar
el programa, tengo que recordar las funciones y las cadena de códigos. 
