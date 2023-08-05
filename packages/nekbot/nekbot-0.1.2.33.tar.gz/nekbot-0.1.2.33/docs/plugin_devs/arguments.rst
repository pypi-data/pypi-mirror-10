.. arguments:

.. highlight:: python

Argumentos en los comandos
##########################
El sistema de argumentos de NekBot para los comandos es bastante sencillo, pero es válido para el 99% de los casos.
Fue concebido para facilitar la sintaxis al extremo, y reducir la cantidad de código necesario al máximo.

La definición de los argumentos se establece en 2 partes:

    * **En el decorador commands**: Exclusivo para establecer los tipos.
    * **En los argumentos de la función**: Nombres de los argumentos, valores por defecto, y tipos en los kwargs (si
    fuese posible) si no están establecidos en el decorador.

Ejemplo::

    @command('random', Num(min=0), Num)
    def random(msg, nmin, nmax): # nmin=Num(min=0) nmax=Num
        if nmin >= nmax:
            raise InvalidArgument('El segundo argumento debe ser mayor al primero.', (nmin, nmax))
        return randint(nmin, nmax)

Ejecutándose como::

    !random <num 1> <num2>

Si no hay tipos definidos en el decorador, NekBot seguirá la siguiente pauta:

#. Si es un argumento con valor por defecto (kwarg), mirará qué valor es este, e intentará obtener la clase o tipo del
 mismo (por ejemplo, int). Hará un call de la clase al valor entregado, y lo devolverá (por ejemplo, int(valor)).
#. En cualquier otra situación, como para los argumentos posicionales, los tratará como strings.

Ejemplo::

    @command
    def random(msg, nmin=0, nmax=6): # nmin=Num(min=0) nmax=Num
        if nmin < 0:
            raise InvalidArgument('Debe ser mayor o igual que cero.', nmin, 0) # msg, val, pos.
        if nmin >= nmax:
            raise InvalidArgument('El segundo argumento debe ser mayor al primero.', (nmin, nmax))
        return randint(nmin, nmax)

El anterior ejemplo, podrá ejecutarse con cualquiera de las 3 siguientes formas::

    !random # entre 0 y 6
    !random <min> # entre min y 6
    !random <min> <max> # entre min y max

Lo siguiente es equivalente a lo anterior::

    @command('random', min=int, max=int)
    def random(msg, nmin=0, nmax=6):
        ...

Casos de excepción
==================
NekBot no solo transforma el valor al tipo deseado. También impide la entrada de argumentos no deseados. Pueden
producirse excepciones por los siguientes casos:

    * No se ha satisfecho el mínimo de argumentos posicionales necesarios.
    * Se ha superado el máximo de argumentos posiciones y de valores por defecto.
    * La transformación de uno de los tipos ha fallado.
    * Las reglas especiales de validación para el tipo no se cumplen.

Argumentos especiales
=====================
