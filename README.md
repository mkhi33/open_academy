# Construcción de un módulo en odoo
---

Odoo proporciona un mecanismo para ayudar a configurar un nuevo módulo:

    odoo-bin scaffold <Nombre del módulo> <Ruta donde se creara el módulo>

## Ejercicio 1: Creación de módulos
`    Use la línea de comando anterior para crear un módulo Open Academy vacío e instálelo en Odoo.`

  - Creación del esqueleto:
  
    ![Texto alternativo](screenshots/1.png "Comando para crear el esqueleto del módulo")
    

## Ejercicio 2: Definir un módulo
`    Defina un nuevo modelo de datos Curso en el módulo de openacademy . Un curso tiene un título y una descripción. Los cursos deben tener un título`.

  - Definiendo un módulo 'Curse'
  
    ![Texto alternativo](screenshots/2.png "definiendo un módulo")

  - Visualización del módulo creado
    ![Texto alternativo](screenshots/install.png "Visualizando un módulo")
  

## Ejercicio 3: Definir datos de demostración
    
`Cree datos de demostración llenando el modelo de Cursos con algunos cursos de demostración.`

  - Creando y definiendo un vista para crear datos de demostración con el modelo de cursos:
  
  ![Texto Alternativo](screenshots/4.png "Creando datos de muestra en la vista course.xml")


## Ejercicio 4: Definir nuevas entradas de menú

`Defina nuevas entradas de menú para acceder a los cursos en la entrada de menú de OpenAcademy. Un usuario debe ser capaz de:`
  - Mostrar una lista de todos los cursos
  - Crear/Modificar cursos


  Definiendo una acción en el archivo `open_academy/views/open_academy_menu.xml`

  ![Texto Alternativo](screenshots/7.png "creando la accion para los cursos")

  Creando un archivo `open_academy/views/open_academy_menu.xml` con los ménus para activar las acciones definidas.

  ![Texto Alternativo](screenshots/5.png "creando el archivo open_academy_menu.xml")


  Agregando el nuevo archivo al `__manifest__.py`

  ![Texto Alternativo](screenshots/6.png "Agregando el archivo al __manifest__.py")
  
1. Mostrando la lista con todos los cursos:
  ![Texto Alternativo](screenshots/8.png "Mostrando lista con todos los cursos")

2. Creando un curso:
  ![Texto Alternativo](screenshots/9.png "Creando un nuevo curso")
3. Editando un curso
  ![Texto Alternativo](screenshots/10.png "Editando un curso")
  ![Texto Alternativo](screenshots/11.png "Editando y guardando un curso")
  ![Texto Alternativo](screenshots/12.png "Lista de cursos")


## Ejercicio 5: Personalizar la vista del formulario usando XML
`Cree su propia vista de formulario para el objeto Curso. Los datos mostrados deben ser: el nombre y la descripción del curso.`

  ![Texto Alternativo](screenshots/13.png "Creando una vista personalizada del formulario")
  ![Texto Alternativo](screenshots/14.png "Creando una vista personalizada del formulario")

## Ejercicio 6: Notebooks
`En la vista de formulario del curso, coloque el campo de descripción debajo de una pestaña, de modo que sea más fácil agregar otras pestañas más adelante, que contengan información adicional.`

  ![Texto Alternativo](screenshots/15.png "Utilizando los notebooks")
  
## Ejercicio 7: Buscar Cursos
`Permitir la búsqueda de cursos en función de su título o su descripción.`
  ![Texto Alternativo](screenshots/16.png "Agregando un buscador por Descripción y Nombre")

## Ejercicio 8: Crear un modelo de sesión
`Para el módulo Open Academy, consideramos un modelo para sesiones : una sesión es una ocurrencia de un curso impartido en un momento dado para una audiencia determinada.`

`Crear un modelo para las sesiones . Una sesión tiene un nombre, una fecha de inicio, una duración y un número de asientos. Agregue una acción y un elemento de menú para mostrarlos. Haga que el nuevo modelo sea visible a través de un elemento de menú.`

- Resultado: 
  ![Texto Alternativo](screenshots/17.png "Mostrando el menú session")
  ![Texto Alternativo](screenshots/18.png "Mostrando la vista del modelo session")

## Ejercicio 9: Relaciones muchos a uno
`Usando many2one, modifique los modelos Course y Session para reflejar su relación con otros modelos:`
- Un curso tiene un usuario responsable ; el valor de ese campo es un registro del modelo incorporado res.users.

- Una sesión tiene un instructor ; el valor de ese campo es un registro del modelo incorporado res.partner.

- Una sesión está relacionada con un curso ; el valor de ese campo es un registro del modelo openacademy.coursey es obligatorio.

- Adaptar las vistas.

Resultado:
  ![Texto Alternativo](screenshots/19.png "Cursos")
  ![Texto Alternativo](screenshots/20.png "Sessiones")

# Ejercicio 10: Relaciones inversas uno a muchos
`Usando el campo relacional inverso one2many, modifique los modelos para reflejar la relación entre cursos y sesiones.`

Resultado: 
  ![Texto Alternativo](screenshots/21.png "Cursos")

# Ejercicio 11: Relaciones Many2Many múltiples
  Utilizando el campo relacional Many2Many, modifica el modelo de Session para relacionar cada sesión a un conjunto de asistentes (attendees). Los asistentes estarán representados por los registros partners, por lo que se relacionan con el modelo res.partner. Adapta las vistas en consecuencia.

Resultado:
  ![Texto Alternativo](screenshots/22.png "Cursos")

# Ejercicio 12: Alterar el contenido existente
- Usando la herencia del modelo, modifique el modelo de socio existente para agregar un instructorcampo booleano y un campo many2many que corresponda a la relación sesión-socio

- Usando la herencia de vista, muestre estos campos en la vista de formulario de socio

Resultado:
  ![Texto Alternativo](screenshots/23.png "Cursos")

# Ejercicio 13: Dominios en campos relacionales

Al seleccionar el instructor para una sesión , solo deben estar visibles los instructores (socios con el valor instructor establecido en ).True deben ser visibles 

Resultado:
  ![Texto Alternativo](screenshots/25.png "Cursos")

# Ejercicio 14: Dominios más complejos

Crear nuevas categorías de socios Profesor / Nivel 1 y Profesor / Nivel 2 . El instructor de una sesión puede ser un instructor o un profesor (de cualquier nivel).

Resultado:
  ![Texto Alternativo](screenshots/26.png "Cursos")
  ![Texto Alternativo](screenshots/27.png "Cursos")
  ![Texto Alternativo](screenshots/28.png "Cursos")

# Ejercicio 15: Campos calculados

- Agregue el porcentaje de asientos ocupados al modelo de sesión

- Mostrar ese campo en las vistas de árbol y formulario

- Mostrar el campo como una barra de progreso

Resultado:
  ![Texto Alternativo](screenshots/29.png "Campos calculados")

# Ejercicio 16: Objetos activos: valores predeterminados

- Defina el valor predeterminado de start_date como hoy (ver Date).

- Agregue un campo activeen la clase Sesión y configure las sesiones como activas de forma predeterminada.
  ![Texto Alternativo](screenshots/30.png "Valores predeterminados y objetos activos")

# Ejercicio 17: Advertencia

- Agregue un onchange explícito para advertir sobre valores no válidos, como un número negativo de asientos o más participantes que asientos.

Resultado:
  ![Texto Alternativo](screenshots/31.png "Valores predeterminados y objetos activos")
  ![Texto Alternativo](screenshots/32.png "Valores predeterminados y objetos activos")

# Ejercicio 18: Agregar restricciones de Python

 - Agregue una restricción que verifique que el instructor no esté presente en los asistentes de su propia sesión.

Resultado:
  ![Texto Alternativo](screenshots/33.png "Restricciones")

# Ejercicio 19: Agregar restricciones de SQL

Con la ayuda de la documentación de PostgreSQL , agregue las siguientes restricciones:

- VERIFIQUE que la descripción del curso y el título del curso sean diferentes

- Haz que el nombre del curso sea ÚNICO

Resultado: 
  ![Texto Alternativo](screenshots/34.png "Restricciones Postgresql")
  ![Texto Alternativo](screenshots/35.png "Restricciones Postgresql")

# Ejercicio 20: Ejercicio 6: agregar una opción duplicada

Dado que agregamos una restricción para la unicidad del nombre del curso, ya no es posible usar la función «duplicar» ( Formulario ‣ Duplicar ).

Vuelva a implementar su propio método de «copia» que permite duplicar el objeto del curso, cambiando el nombre original a «Copia de [nombre original]».

Resultado:
  ![Texto Alternativo](screenshots/36.png "Implementando un metodo de copia personalizado para los cursos")

# Ejercicio 21: Lista para colorear

Modifique la vista de árbol de sesión de tal manera que las sesiones que duren menos de 5 días se coloreen de azul y las que duren más de 15 días se coloreen de rojo.

Resultado:
  ![Texto Alternativo](screenshots/37.png "Cambiando color a una sesión segun su duración")
  ![Texto Alternativo](screenshots/38.png "Cambiando color a una sesión segun su duración")

# Ejercicio 22: Vista de calendario

Agregue una vista de calendario al modelo de sesión que permita al usuario ver los eventos asociados a Open Academy.
Resultado: 
  ![Texto Alternativo](screenshots/39.png "Cambiando color a una sesión segun su duración")

# Ejercicio 23: Vistas de búsqueda

- Agregue un botón para filtrar los cursos de los que el usuario actual es responsable en la vista de búsqueda de cursos. Hágalo seleccionado por defecto.

- Agregue un botón para agrupar cursos por usuario responsable.
  Resultado:
  ![Texto Alternativo](screenshots/40.png "Cambiando color a una sesión segun su duración")

# Ejercicio 24: diagramas de Gantt

Agregue un diagrama de Gantt que le permita al usuario ver la programación de sesiones vinculada al módulo Open Academy. Las sesiones deben agruparse por instructor.

Resultado:

      La vista de Gantt requiere el módulo web_gantt que está presente en la versión de edición empresarial .

# Ejercicio 25: Vistas en Gráfico

- Agrega una vista de gráfico en el objeto Session que muestre, para cada curso, el número de participantes bajo la forma de un gráfico de barras.

- Agrega el número de asistentes como un campo calculado almacenado

- Luego añade la vista relevante
  
Resultado:

![Texto Alternativo](screenshots/41.png "Mostrando un gráfico")

# Ejercicio 26: Vista Kanban

- Agregue una vista Kanban que muestre las sesiones agrupadas por curso (por lo tanto, las columnas son cursos).
  
Resultado:
![Texto Alternativo](screenshots/42.png "Mostrando un kanban")

# Ejercicio 27: Añade control de acceso mediante la interfaz de Odoo

Crea un nuevo usuario «John Smith». Luego cree un grupo «OpenAcademy / Session Read» con acceso de lectura al modelo de sesión .

Resultado:

![Texto Alternativo](screenshots/43.png "Creando usuario")
![Texto Alternativo](screenshots/43.png "Creando grupo y asignando permisos")
![Texto Alternativo](screenshots/44.png "Agregando el usuario al grupo")

# Ejercicio 28: Añade el control de acceso a través de los archivos de datos en el módulo

- Utilizando archivos de datos, Cree un grupo OpenAcademy / Manager con acceso completo a todos los modelos de OpenAcademy

- Hacer que la sesión y el curso sean legibles para todos los usuarios

Resultado:
![Texto Alternativo](screenshots/45.png "Utilizando seguridad")

# Ejercicio 29: Regla de registro

Agrega una regla de registro para el Curso modelo y el grupo «OpenAcademy / Manager», que restringe writey unlinkaccede a los responsables de un curso. Si un curso no tiene responsable, todos los usuarios del grupo deben poder modificarlo.

Resultado: 
![Texto Alternativo](screenshots/46.png "Creando una nueva regla de registro")

# Ejercicio 30: Definir el asistente

Cree un modelo de asistente con una relación many2one con el modelo Session y una relación many2many con el modelo Partner .

Resultado:
![Texto Alternativo](screenshots/48.png "Creando una nueva regla de registro")

# Ejercicio 31: Iniciar el asistente

- Defina una vista de formulario para el asistente.

- Agregue la acción para iniciarla en el contexto del modelo de sesión .

- Defina un valor predeterminado para el campo de sesión en el asistente; utilice el parámetro de contexto self._contextpara recuperar la sesión actual.

Resultado:
![Texto Alternativo](screenshots/49.png "Wizard")

# Ejercicio 32: Registrar asistentes

Agregue botones al asistente e implemente el método correspondiente para agregar asistentes a la sesión dada.

Resultado:
![Texto Alternativo](screenshots/51.png "Wizard")

# Ejercicio 33: Registrar asistentes a múltiples sesiones

Modifique el modelo del asistente para que los asistentes puedan registrarse en varias sesiones.

Resultado:
![Texto Alternativo](screenshots/52.png "Wizard")

# Ejercicio 34: Traducir un módulo

Elija un segundo idioma para su instalación de Odoo. Traduzca su módulo usando las facilidades provistas por Odoo.

Resultado:
![Texto Alternativo](screenshots/53.png "Internacionalización")
![Texto Alternativo](screenshots/54.png "Internacionalización")
![Texto Alternativo](screenshots/55.png "Internacionalización")
![Texto Alternativo](screenshots/56.png "Internacionalización")
![Texto Alternativo](screenshots/57.png "Internacionalización")

# Ejercicio 35: Crear un informe para el modelo de sesión

Para cada sesión, debe mostrar el nombre de la sesión, su inicio y fin, y una lista de los asistentes a la sesión.


# Ejercicio 36: Definir un tablero

Defina un tablero que contenga la vista de gráfico que creó, la vista de calendario de sesiones y una vista de lista de los cursos (conmutable a una vista de formulario). Este tablero debe estar disponible a través de un elemento de menú en el menú y mostrarse automáticamente en el cliente web cuando se selecciona el menú principal de OpenAcademy.



