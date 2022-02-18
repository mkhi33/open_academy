# Construcción de un módulo en odoo
---

Odoo proporciona un mecanismo para ayudar a configurar un nuevo módulo:

    odoo-bin scaffold <Nombre del módulo> <Ruta donde se creara el módulo>

## Ejercicio 1: Creación de módulos
`    Use la línea de comando anterior para crear un módulo Open Academy vacío e instálelo en Odoo.`

  - Creación del esqueleto:
  
    ![Texto alternativo]([img1]:../../screenshots/1.png "Comando para crear el esqueleto del módulo")
    

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

  ![Texto Alternativo]([img1]:../../screenshots/16.png "Utilizando los notebooks")
  

    