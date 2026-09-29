# Proyecto 3 – Katas Python

Resolución de las 40 katas del Proyecto 3. Todas las katas están en un único archivo, `katas_python.py`, y cada una va encabezada por su enunciado en un comentario.

## Contenido del repositorio

| Archivo | Descripción |
| --- | --- |
| `katas_python.py` | Las 40 katas resueltas, con comentarios, ejemplos y pruebas |
| `README.md` | Este documento: estructura del proyecto y pasos seguidos |

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta del proyecto:

```bash
python katas_python.py
```

Si todo funciona, cada kata muestra su ejemplo y las que tienen pruebas terminan con el mensaje `Kata N OK`.

Las funciones que piden datos por teclado (`pedir_y_dividir`, `pedir_edad`, `buscar_nombre`, `indicar_momento_dia`, `calificacion_texto` y `calcular_compra`) no se llaman al ejecutar el archivo, para que se ejecute de principio a fin sin detenerse. Para probarlas de forma interactiva:

```bash
python -i katas_python.py
```

La opción `-i` ejecuta el archivo y deja abierto el intérprete con todas las funciones cargadas. Desde ahí se puede llamar a cualquiera de ellas, por ejemplo `indicar_momento_dia()`.

## Estructura de cada kata

Todas las katas siguen el mismo esquema:

1. **Enunciado** en un comentario.
2. **Comentario explicativo** con las decisiones tomadas y los pasos que más me han costado.
3. **Código** de la solución.
4. **Ejemplo** con `print` para ver el resultado al ejecutar.
5. **Pruebas** con `assert` y el mensaje `Kata N OK` (excepto en las katas que dependen de `input()`, ver [Validación](#validación)).

## Pasos seguidos

1. **Primera resolución** de las 40 katas.
2. **Revisión kata a kata**: comprobé que cada solución cumpliera el enunciado y estudié qué casos límite podían fallar (listas vacías, mayúsculas, valores fuera de rango, texto donde se esperan números…).
3. **Corrección** solo de lo que no cumplía el enunciado o daba un resultado incorrecto. Si una kata ya cumplía, la mantuve tal cual.
4. **Validación** de cada kata con 2 o 3 pruebas `assert`: un caso normal y uno o dos casos límite.
5. **Limpieza** del código: nombres de variables, comentarios y formato.

## Convenciones del código

- **Sufijo `_kataN` en las variables de ejemplo** (`empleados_kata32`, `numeros_kata19`…). Como las 40 katas están en el mismo archivo, todas las variables creadas fuera de una función comparten el mismo espacio de nombres. Si dos katas usaran el mismo nombre, la segunda sobrescribiría a la primera sin avisar. El sufijo mantiene cada nombre único y deja claro a qué kata pertenece. Las variables definidas dentro de las funciones no lo necesitan, porque son locales.
- **Nombres en `snake_case`** y en español, según PEP 8.
- **Datos de ejemplo distintos** de los usados durante la resolución, para comprobar que cada función sirve con cualquier dato y no solo con uno concreto.

## Validación

- Cada kata tiene entre 2 y 3 pruebas `assert`. Si una prueba falla, el programa se detiene con `AssertionError` e indica en qué kata está el problema.
- Los errores que las funciones deben lanzar se comprueban con `try` / `except`.
- Las katas 31, 37, 38 y 40 dependen de `input()` y no admiten `assert`. Se han probado a mano con `python -i` y, en lugar de pruebas, muestran un ejemplo de su lógica con datos fijos.

## Uso de IA

He utilizado Claude como corrector y asistente durante el proyecto:

- **Corrector:** revisar que cada solución cumpliera el enunciado y detectar casos en los que el código fallaba.
- **Asistente:** explicar el funcionamiento de cada solución y resolver dudas durante el desarrollo.
- **Integración de comentarios y pruebas:** redactar los comentarios explicativos e incorporar las pruebas `assert` de validación.

Todo el código entregado lo he revisado y entiendo cada uno de sus pasos.
