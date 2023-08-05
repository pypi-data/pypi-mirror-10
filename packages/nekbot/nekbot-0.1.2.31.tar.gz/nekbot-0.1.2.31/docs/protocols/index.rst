
Protocolos
##########

+==============================+=====+========+==========+
|        Característica        | IRC | Jabber | Telegram |
+==============================+=====+========+==========+
| Salas de chat                | X   | X      | X        |
+------------------------------+-----+--------+----------+
| Conversaciones privadas      |     | X      |          |
| en sala de chat              |     |        |          |
+------------------------------+-----+--------+----------+
| Conversaciones privadas      | X   | X      | X        |
| fuera de salas               |     |        |          |
+------------------------------+-----+--------+----------+
| Listado de amigos fuera      |     | X      | X        |
| de salas de chat             |     |        |          |
+------------------------------+-----+--------+----------+
| Saltos de línea en           |     | X      | X        |
| mensajes                     |     |        |          |
+------------------------------+-----+--------+----------+
| Soporte unicode completo     |     | X      | X        |
+------------------------------+-----+--------+----------+
| Sin limitaciones en nombres  |     | X      | X        |
| de los usuarios              |     |        |          |
+------------------------------+-----+--------+----------+
| Identificación de usuarios   | [1] | [2]    | X        |
| en salas de chat             |     |        |          |
+------------------------------+-----+--------+----------+
| Identificación de usuarios   | [1] | X      | X        |
| fuera de salas de chat       |     |        |          |
+------------------------------+-----+--------+----------+
| Histórico de mensajes en     |     | [3]    | X        |
| salas de chat                |     |        |          |
+------------------------------+-----+--------+----------+
| Mensajes privados visibles   | X   |        |          |
| en sala de chat (NOTICE)     |     |        |          |
+------------------------------+-----+--------+----------+
| Listado de usuarios del      | X   | [4]    |          |
| servidor                     |     |        |          |
+------------------------------+-----+--------+----------+
| Broadcast a amigos de lista  |     | [5]    | X        |
| de amigos                    |     |        |          |
+------------------------------+-----+--------+----------+
| Envío de archivos a amigos   |     | X      | X        |
+------------------------------+-----+--------+----------+
| Envío de archivos en salas   |     |        | X        |
| de chat                      |     |        |          |
+------------------------------+-----+--------+----------+
| Envío de archivos multimedia |     |        | X        |
+------------------------------+-----+--------+----------+
| Envío de geolocalización     |     | X      | X        |
+------------------------------+-----+--------+----------+

1. En IRC, los usuarios pueden registrar su nick para tener prioridad al usarlos, pero ello no quita que otros no puedan usarlo. Se debe usar otros métodos, como consultar a NickServ, para comprobar si el usuario es quien afirma ser.
2. Algunas salas de chat pueden tener parametrado que los usuarios no puedan ver los JIDs (identificador único) de otras personas. Si el bot es administrado, esto no aplica. Igualmente, existen en algunos servidores formas de registrar un nick para salas, de forma que nadie más pueda usarlo.
3. En Jabber, el histórico sólo es recuperable, por lo general, un limitado número de líneas antes de la llegada. Esto se solucionaría con el XEP-0313, el cual todavía es experimental.
4. Algunos servidores cuentan con un servicio para buscar en los usuarios del servidor, pero no un listado completo de los mismos (por privacidad).
5. No cuenta con broadcast, pero sí con lista de amigos, por lo que se puede envuar a cada uno de ellos individualmente.
