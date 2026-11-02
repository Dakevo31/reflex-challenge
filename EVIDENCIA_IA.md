# Evidencia de Vibecoding – Reflex Challenge

## 1. Objetivo

Desarrollar un mini-juego funcional en Python utilizando inteligencia artificial como copiloto de programación, aplicando un proceso iterativo de generación, validación y mejora del código.

## 2. Prompts utilizados

### Prompt 1: Desarrollo inicial

**Solicitud:** Actúa como desarrollador senior de Python y Tkinter. Crea un mini-juego llamado Reflex Challenge en un único archivo `main.py`, con pantalla inicial, temporizador de 30 segundos, círculos en posiciones aleatorias, 10 puntos por acierto, pantalla de resultados, opción de volver a jugar y registro del mejor puntaje durante la sesión. Utiliza `after()` para el temporizador, evita que los objetivos aparezcan fuera del área de juego y no utilices librerías externas.

**Objetivo:** Obtener una primera versión funcional que permitiera validar las mecánicas principales del juego.

**Resultado:** Se desarrolló una aplicación con interfaz gráfica, sistema de puntuación, temporizador y navegación entre pantallas.

### Prompt 2: Mejora de la experiencia

**Solicitud:** Mejora el código existente de Reflex Challenge sin reconstruirlo desde cero. Implementa dificultad progresiva reduciendo el tamaño de los objetivos conforme aumenta la puntuación, muestra brevemente un indicador +10 después de cada acierto y mejora la pantalla final con un mensaje especial cuando se supera el récord. Conserva todas las funcionalidades existentes.

**Objetivo:** Hacer el juego más desafiante y proporcionar retroalimentación visual al jugador.

**Resultado:** Se incorporaron dificultad progresiva, indicador de puntuación y mensajes diferenciados en la pantalla de resultados.

### Prompt 3: Animación de fuegos artificiales

**Solicitud:** Agrega una pequeña explosión de partículas de colores alrededor del punto donde el jugador acierta un círculo. El efecto debe durar aproximadamente medio segundo, permanecer localizado, permitir múltiples animaciones simultáneas y utilizar únicamente Tkinter Canvas y `after()`. Las animaciones pendientes deben cancelarse al finalizar la partida.

**Objetivo:** Mejorar la experiencia visual sin afectar el rendimiento ni modificar la mecánica principal.

**Resultado:** Se implementó una animación de partículas acompañada del indicador +10.

## 3. Refinamiento adicional

Durante la revisión de las mejoras se identificó que los círculos mantenían un mismo tamaño para cada nivel de puntuación, lo que hacía que el desafío fuera predecible.

Se solicitó modificar `get_target_radius()` para generar radios aleatorios dentro de un rango permitido, conservando la dificultad progresiva.

**Resultado:** Los objetivos aparecen con tamaños grandes, medianos o pequeños de manera aleatoria.

Este ajuste demuestra que el código generado por IA fue revisado y refinado según la experiencia de uso.

## 4. Validación y pruebas

Se realizaron pruebas manuales ejecutando `python main.py`.

Se verificó el inicio del juego, el funcionamiento del temporizador, la puntuación por acierto, la aparición de objetivos dentro del área de juego, los botones de navegación y la conservación del récord entre partidas.

También se comprobaron los efectos visuales y la variación de tamaños de los círculos.

**Limitación identificada:** El récord se conserva únicamente durante la sesión de ejecución. No se implementó almacenamiento permanente porque no era necesario para el alcance definido.

**Ajuste realizado:** Se modificó la generación del tamaño de los objetivos para evitar que todos tuvieran el mismo radio dentro de un mismo nivel de dificultad.

## 5. Reflexión final

El desarrollo de Reflex Challenge permitió comprender cómo utilizar la inteligencia artificial como herramienta de apoyo para construir una aplicación funcional.

Una de las principales ventajas fue la rapidez para generar una estructura inicial y realizar mejoras específicas mediante prompts.

También se identificó que la IA no reemplaza la validación del desarrollador. Fue necesario ejecutar el juego, revisar su comportamiento y solicitar ajustes cuando el resultado no coincidía completamente con la experiencia esperada.

Durante el proyecto se reforzaron conceptos de programación orientada a objetos, eventos de interfaz gráfica, generación de valores aleatorios y programación de tareas mediante `after()`.

Las áreas que requieren mayor práctica son la gestión de animaciones, los callbacks y la organización de aplicaciones gráficas más complejas.

En conclusión, el vibecoding permitió acelerar el desarrollo, mientras que las pruebas y las decisiones sobre las mejoras ayudaron a mantener el control sobre el resultado final.