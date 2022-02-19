# Construcción de un módulo en odoo
---

Odoo proporciona un mecanismo para ayudar a configurar un nuevo módulo:

    odoo-bin scaffold <Nombre del módulo> <Ruta donde se creara el módulo>

## Ejercicio 1: Creación de módulos
`    Use la línea de comando anterior para crear un módulo Open Academy vacío e instálelo en Odoo.`

  - Creación del esqueleto:
  
    ![Texto alternativo]([img1]:./open_academy/screenshots/1.png "Comando para crear el esqueleto del módulo")
    

## Ejercicio 2: Definir un módulo
`    Defina un nuevo modelo de datos Curso en el módulo de openacademy . Un curso tiene un título y una descripción. Los cursos deben tener un título`.

  - Definiendo un módulo 'Curse'
  
    ![Texto alternativo]([img2]:../../screenshots/2.png "definiendo un módulo")

  - Visualización del módulo creado
    ![Texto alternativo]([img2]:../../screenshots/install.png "Visualizando un módulo")
  

## Ejercicio 3: Definir datos de demostración
    
`Cree datos de demostración llenando el modelo de Cursos con algunos cursos de demostración.`

  - Creando y definiendo un vista para crear datos de demostración con el modelo de cursos:
  
  ![Texto Alternativo]([img1]:../../screenshots/4.png "Creando datos de muestra en la vista course.xml")


## Ejercicio 4: Definir nuevas entradas de menú

`Defina nuevas entradas de menú para acceder a los cursos en la entrada de menú de OpenAcademy. Un usuario debe ser capaz de:`
  - Mostrar una lista de todos los cursos
  - Crear/Modificar cursos


  Definiendo una acción en el archivo `open_academy/views/open_academy_menu.xml`

  ![Texto Alternativo]([img1]:../../screenshots/7.png "creando la accion para los cursos")

  Creando un archivo `open_academy/views/open_academy_menu.xml` con los ménus para activar las acciones definidas.

  ![Texto Alternativo]([img1]:../../screenshots/5.png "creando el archivo open_academy_menu.xml")


  Agregando el nuevo archivo al `__manifest__.py`

  ![Texto Alternativo]([img1]:../../screenshots/6.png "Agregando el archivo al __manifest__.py")
  
1. Mostrando la lista con todos los cursos:
  ![Texto Alternativo]([img1]:../../screenshots/8.png "Mostrando lista con todos los cursos")

2. Creando un curso:
  ![Texto Alternativo]([img1]:../../screenshots/9.png "Creando un nuevo curso")
3. Editando un curso
  ![Texto Alternativo]([img1]:../../screenshots/10.png "Editando un curso")
  ![Texto Alternativo]([img1]:../../screenshots/11.png "Editando y guardando un curso")
  ![Texto Alternativo]([img1]:../../screenshots/12.png "Lista de cursos")


## Ejercicio 5: Personalizar la vista del formulario usando XML
`Cree su propia vista de formulario para el objeto Curso. Los datos mostrados deben ser: el nombre y la descripción del curso.`

  ![Texto Alternativo]([img1]:../../screenshots/13.png "Creando una vista personalizada del formulario")
  ![Texto Alternativo]([img1]:../../screenshots/14.png "Creando una vista personalizada del formulario")

## Ejercicio 6: Notebooks
`En la vista de formulario del curso, coloque el campo de descripción debajo de una pestaña, de modo que sea más fácil agregar otras pestañas más adelante, que contengan información adicional.`

  ![Texto Alternativo]([img1]:../../screenshots/15.png "Utilizando los notebooks")
  
## Ejercicio 7: Buscar Cursos
`Permitir la búsqueda de cursos en función de su título o su descripción.`
  ![Texto Alternativo]([img1]:../../screenshots/16.png "Agregando un buscador por Descripción y Nombre")

## Ejercicio 8: Crear un modelo de sesión
`Para el módulo Open Academy, consideramos un modelo para sesiones : una sesión es una ocurrencia de un curso impartido en un momento dado para una audiencia determinada.`

`Crear un modelo para las sesiones . Una sesión tiene un nombre, una fecha de inicio, una duración y un número de asientos. Agregue una acción y un elemento de menú para mostrarlos. Haga que el nuevo modelo sea visible a través de un elemento de menú.`

- Resultado: 
  ![Texto Alternativo]([img1]:../../screenshots/17.png "Mostrando el menú session")
  ![Texto Alternativo]([img1]:../../screenshots/18.png "Mostrando la vista del modelo session")

## Ejercicio 9: Relaciones muchos a uno
`Usando many2one, modifique los modelos Course y Session para reflejar su relación con otros modelos:`
- Un curso tiene un usuario responsable ; el valor de ese campo es un registro del modelo incorporado res.users.

- Una sesión tiene un instructor ; el valor de ese campo es un registro del modelo incorporado res.partner.

- Una sesión está relacionada con un curso ; el valor de ese campo es un registro del modelo openacademy.coursey es obligatorio.

- Adaptar las vistas.

Resultado:
  ![Texto Alternativo]([img1]:../../screenshots/19.png "Cursos")
  ![Texto Alternativo]([img1]:../../screenshots/20.png "Sessiones")

# Ejercicio 10: Relaciones inversas uno a muchos
`Usando el campo relacional inverso one2many, modifique los modelos para reflejar la relación entre cursos y sesiones.`

Resultado: 
  ![Texto Alternativo]([img1]:../../screenshots/21.png "Cursos")

# Ejercicio 11: Relaciones Many2Many múltiples
  Utilizando el campo relacional Many2Many, modifica el modelo de Session para relacionar cada sesión a un conjunto de asistentes (attendees). Los asistentes estarán representados por los registros partners, por lo que se relacionan con el modelo res.partner. Adapta las vistas en consecuencia.

Resultado:
  ![Texto Alternativo]([img1]:../../screenshots/22.png "Cursos")

# Ejercicio 12: Alterar el contenido existente
- Usando la herencia del modelo, modifique el modelo de socio existente para agregar un instructorcampo booleano y un campo many2many que corresponda a la relación sesión-socio

- Usando la herencia de vista, muestre estos campos en la vista de formulario de socio

Resultado:
  ![Texto Alternativo]([img1]:../../screenshots/23.png "Cursos")

# Ejercicio 13: Dominios en campos relacionales

Al seleccionar el instructor para una sesión , solo deben estar visibles los instructores (socios con el valor instructor establecido en ).True deben ser visibles 

Resultado:
  ![Texto Alternativo]([img1]:../../screenshots/25.png "Cursos")

# Ejercicio 14: Dominios más complejos

Crear nuevas categorías de socios Profesor / Nivel 1 y Profesor / Nivel 2 . El instructor de una sesión puede ser un instructor o un profesor (de cualquier nivel).

Resultado:
  ![Texto Alternativo]([img1]:../../screenshots/26.png "Cursos")
  ![Texto Alternativo]([img1]:../../screenshots/27.png "Cursos")
  ![Texto Alternativo]([img1]:../../screenshots/28.png "Cursos")
