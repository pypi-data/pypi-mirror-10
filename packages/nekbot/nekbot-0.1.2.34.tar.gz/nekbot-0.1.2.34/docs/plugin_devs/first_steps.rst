.. first_steps:

.. highlight:: python

Mi primer plugin
################
¡Crear un plugin es fácil, rápido, y para toda la familia! En serio, es tan fácil que te sentirás insultado. Procura
no ofenderte mucho.

1. Primero, crea un archivo de plugin en el directorio "plugins" de tu proyecto. Por ejemplo, "hello.py".
2. Pon lo siguiente en el archivo::

    from nekbot.core.commands import command

    @command
    def hello(message):
        return 'Hello world! Your message: %s' % message

3. Pon el nombre del archivo (sin el .py) en el PLUGINS del archivo settings.py de tu proyecto y... ¡Listo! Ahora
puedes ejecutar el comando "!hello" en una sala o conversación donde esté tu bot, y devolverá el texto del return.

Si quisieses poner un nombre no permitido por Python (guiones, palabras reservas, etc.), puedes emplear en el
decorador::

    @command('my-command')
    def my_command(message):
        pass


Argumentos posicionales
=======================
NekBot permite añadir argumentos de una forma fácil a tus comandos. ¡Y es tan fácil como usar los propios argumentos
de tus funciones!

Argumentos posicionales

Por ejemplo, el siguiente comando exigirá un argumento (obligatorio)::

    @command
    def greet(message, person):
        return '¡Hola %s!' % person

Lo cual se ejecutará con::

    !greet Pepe

Por supuesto, también podemos usar `*args`::

    @command
    def greet(message, *args):
        return '¡Hola %s!' % ', '.join(args)

Lo cual se usará con::

    !greet Pepe "José Pérez" Fernando

Validación
==========
Por supuesto, de nada sirve obtener valores, si estos no nos sirve. NekBot tiene un sistema que se encarga de
comprobar la validez de dichos datos, transformarlos, y mostrar un error en caso de no ser correctos. Por ejemplo, la
siguiente función solo funcionará si los valores son números::

    from random import randint

    @command('random', int, int)
    def random(message, start, end):
        return randint(start, end)

En caso de no devolverse un valor correcto, obtendremos algo como lo siguiente::

    In: !random 3 spam
    Out:El argumento en la posición 2 con valor "spam", no es válido. El valor debe ser un número.

Argumentos por omisión
======================
Como estamos aprovechando el potencial de Python para la validación y la obtención de los valores, no podríamos
olvidar los argumentos por omisión. La diferencia, es que aquí la validación se realiza de forma automática en
función al valor dado por defecto. Así, por ejemplo, en el siguiente caso::

    @command('default-10')
    def default_10(message, number=10):
        return number

Si pusiésemos algo que no fuese permitido por la clase del valor por defecto, nos daría un error::

    In: !default-10 eggs
    Out:El argumento en la posición 1 con valor "eggs", no es válido. El valor debe ser un número.

Métodos y propiedades de Message
================================
El primer argumento entregado siempre será uno del tipo Message (en realidad, una clase que hereda de ella, que será
una clase Message específica del protocolo por el cual entró el mensaje). Algunos ejemplos de propiedades son:

    * **message.body:** el mensaje original del usuario que provocó la ejecución del mensaje.
    * **message.user:** clase que hereda User, con propiedades como username o id.
    * **message.groupchat:** clase que hereda de GroupChat, con información de la sala y sus usuarios.

Algunos ejemplos de métodos son:

    * **message.reply(<message string>)**: Mensaje a enviar a la misma conversación que provocó el comando.
    * **message.user.send_message(<message string>)**: Enviar mensaje al usuario por un medio privado.
    * **message.groupchat.send_message(<message string>)**: Enviar mensaje a la sala, donde todos pueden verlo.