.. dev_plugins:

.. highlight:: python

Creación de plugins
####################
Los plugins de NekBot pueden encontrarse en 2 posibles ubicaciones:

    * Directorio "plugins" del directorio en ejecución (el proyecto).
    * Ruta "nekbot/plugins/<plugin>", dentro de NekBot.

En cualquiera de los 2 casos, se importará el archivo de mismo nombre (acabado en .py) del directorio, o el"__init__
.py" dentro de la carpeta con el nombre del bot. Para más información: http://learnpythonthehardway.org/book/ex46.html


Plugins en su directorio de proyecto
====================================
En la mayoría de los casos, para la creación de plugins sencillos para su proyecto, le interesará **la primera forma**
(creando los plugins en su directorio de proyecto de NekBot, es decir, donde va el settings.py, y se encuentra el
directorio plugins, que es el que nos interesa). Creando un archivo con el nombre de su plugin, acabado en ".py",
será suficiente. Si fuese más grande, haga una carpeta con el nombre del plugin, y dentro un archivo "__init__.py"
con las funciones de los comandos que serán interpretados por NekBot.

Ejemplos (respectivamente)::

    plugins/hello.py
    plugins/hello/__init__.py


Plugins distribuidos
====================
Si está pensando en crear un plugin para distribuir, ¡felicidades! Ahora usted forma parte de la comunidad. Para
ayudar a su encomiable labor, hemos creado un subcomando con el ejecutable de nekbot (el mismo que usa para lanzar su
 servidor)::

    nekbot createplugin <ruta>

Tenga en cuenta, que el nombre de la última carpeta, será el nombre del plugin. Por ejemplo::

    nekbot createplugin /home/user/Work/hello

Esto creará por usted una estructura básica de cómo deben ser los plugins, incluyendo un instalador, y todo lo
necesario para distribuirse. Para facilitar su trabajo, puede añadir también los siguientes parámetros al settings de
 su proyecto::

    PLUGIN_AUTHOR_NAME = 'su nombre'
    PLUGIN_AUTHOR_EMAIL = 'su@email'
    PLUGIN_AUTHOR_WEBSITE = 'https://sitioweb'
    HOOK_BEFORE_CREATE_PLUGIN = 'echo Hello'
    HOOK_AFTER_CREATE_PLUGIN = 'python:workflow.create_plugin'

Los 3 primeros parámetros serán datos que se rellenarán automáticamente en la plantilla. Los otros 2, permiten
ejecutar acciones antes y después de crearse el plugin. El último hook permite ejecutar una función de un módulo de
sus sistema (por ejemplo, que se encuentre en su carpeta de trabajo). Esta función recibe como parámetros::

    def create_plugin(dest, name, settings):
        pass

Los hooks le permitirán ahorrar todavía más tiempo al crear plugins. Entre usted y yo, el mío, crea un repositorio
mercurial, lo registra en bitbucket, establece la licencia del plugin, lo registra en Pypi... entre otra infinidad de
 cosas :)

Es muy probable, que para trabajar en su plugin, quiera poder utilizarlo en su entorno de trabajo (su proyecto). Para
 lograrlo, puede hacer un enlace simbólico entre la carpeta del plugin del proyecto de su plugin
 (nekbot/plugins/hello/), y donde debería encontrarse si usa la primera forma (plugins/hello/, en el directorio de su
bot). Esto mismo podría lograrlo con un hook, creando un archivo workflow.py en el directorio de su bot::

    import os

    def create_plugin(dest, name, settings):
        os.symlink(os.path.join(dest, 'nekbot', 'plugins', name),
                   os.path.join('/home/nekmo/Work/mybot/plugins/%s' % name))

Para subir sus archivos a Pypi, siga estas instrucciones: http://peterdowns.com/posts/first-time-with-pypi.html