.. dev_commands:

.. highlight:: python

Creación de comandos
####################
Si está usando un directorio para los plugins, deberá tener en cuenta que los comandos deben encontrarse (o estar
referenciados) en el archivo `__init__.py`. Para más información, vea `dev_plugins`_.

Para especificar que una función es un comando, debe ir con el decorador `@command`::

    @command
    def hello(msg):
        return 'Hello world!'

Lo cual respondería a::

    In: !hello
    Out:Hello world!

Este decorador puede ir sin, o con argumentos, siendo estos los argumentos que recibirá el comando, obviando el
primero, que es el nombre del comando::

    @command('hello', str)
    def hello(msg, greet):
        return 'Hello world, %!' % greet

Ejemplo::

    In: !hello
    Out:Hello world!

Esto puede usarse para establecer nombre de comandos que no podrían utilizarse para el nombre de la función (por
limitaciones de Python)::

    @command('class')
    def class_cmd(msg):
        return 'We have class!'

Para más información sobre los argumentos, vea `arguments`_.

Return y excepciones en comandos
================================
En las funciones de los comandos si no devuelve nada, no se mostrará nada::

    @command
    def hello(msg):
        msg.reply('Hello!')


Si devuelve algo (que no sea None), NekBot intentará interpretarlo como un string::

    @command
    def random_int(msg):
        return random.randint(1,6)

Si se produce una excepción no controlada en un comando, esta será capturada y se mostrará un mensaje de advertencia::

    In: !raise_exception
    Out: Warning: El comando !raise_exception no finalizó correctamente.

No obstante, puede usar (y crear) excepciones que mostrarán un mensaje a su elección::

    from nekbot.core.exceptions import PrintableException

    @command
    def raise_printable_exception(msg):
        raise PrintableException("nobody's specs the spanish inquisition!")

Ejemplo::

    In: !raise_printable_exception
    Out: nobody's specs the spanish inquisition!

Esto último puede ser muy interesante, cuando su plugin es bastante grande, y está compuesto de varias funciones. Si
en una de estas se provoca un PrintableException, el curso de su comando se cortará, pero se mostrará un mensaje
informativo al usuario.

Control en los comandos
=======================
El decorador `@control` es el encargado de filtrar cuando, quien, y en qué contexto, podrá utilizarse el comando. Por
ejemplo, para que solo los usuarios del grupo root puedan usarlo::

    @command
    @control('root')
    def need_root(msg):
        return 'Hola jefe!'

