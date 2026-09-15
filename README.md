# Sistema de Gestión de Solicitudes Técnicas

Práctica de Estructuras de Datos que simula una mesa de ayuda técnica. Las áreas de trabajo se organizan en una pila (`Stack`) y cada área administra sus solicitudes mediante una o dos colas (`Queue`).

## Requisitos

- Python 3.
- No requiere instalar paquetes externos.

## Ejecución

Abre una terminal en la carpeta del proyecto y ejecuta:

```text
python main.py
```

## Áreas iniciales

La pila inicia con este orden de TOP a BASE:

1. Recepción y Triaje, capacidad 4.
2. Diagnóstico Técnico, capacidad 2.
3. Reparación / Corrección, capacidad 2.
4. Control de Calidad y Cierre, capacidad 1.

Las áreas se procesan desde TOP hasta BASE. Una solicitud transferida espera al siguiente turno para ser procesada por el área siguiente.

## Reglas del sistema

- Las prioridades permitidas son `Alta` y `Normal`.
- Recepción y Triaje utiliza una cola para solicitudes Alta y otra para solicitudes Normal.
- En Recepción y Triaje, las solicitudes Alta se procesan antes que las Normal.
- Las demás áreas utilizan una sola cola.
- Un área normal se considera sobrecargada cuando tiene más de 5 solicitudes al inicio del turno.
- Recepción y Triaje no se considera sobrecargada.
- En un área sobrecargada, la capacidad efectiva es la mitad entera de la capacidad base, con mínimo 1.
- Cuando una solicitud llega a Control de Calidad y Cierre y es procesada, termina su recorrido.

## Opciones del menú

1. Registrar una solicitud con ID, descripción y prioridad.
2. Ejecutar un turno manual.
3. Ejecutar turnos automáticamente hasta vaciar el sistema.
4. Eliminar un área y redistribuir sus solicitudes pendientes al área inferior disponible.
5. Agregar una nueva área mediante `push()`.
6. Consultar el estado de las áreas y sus colas.
7. Salir del programa.

## Organización de archivos

- `node.py`: clase `Node` para los nodos de la lista enlazada.
- `slinkedlist.py`: lista enlazada utilizada por las estructuras del proyecto.
- `queue.py`: clase `Queue` con operaciones de cola.
- `stack.py`: clase `Stack` con operaciones de pila.
- `solicitud.py`: clase `Solicitud`.
- `area.py`: clase `Area` y sus colas de solicitudes.
- `sistema.py`: lógica de áreas, turnos, transferencias, sobrecarga y redistribución.
- `main.py`: menú e interacción con el usuario.

## Prueba manual rápida

1. Ejecuta `python main.py`.
2. Selecciona `1` y registra una solicitud Alta.
3. Selecciona `6` para consultar su ubicación inicial.
4. Selecciona `2` varias veces para observar su avance entre áreas.
5. Selecciona `3` para completar automáticamente las solicitudes pendientes.
6. Selecciona `7` para salir.
