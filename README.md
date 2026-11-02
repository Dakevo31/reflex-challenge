# 🎯 Reflex Challenge

**Entrena tus reflejos. Supera tu récord.**

Reflex Challenge es un mini-juego desarrollado en Python utilizando Tkinter, cuyo objetivo es poner a prueba la velocidad de reacción del jugador mediante círculos que aparecen aleatoriamente en pantalla.

Este proyecto fue desarrollado como parte de la actividad **Vibecoding Guiado: Desarrollo de una Aplicación o Mini-Juego con IA como Copiloto**, de KODIGO.

## 🎮 ¿Cómo jugar?

1. Ejecuta la aplicación.
2. Presiona **START GAME**.
3. Haz clic sobre los círculos que aparecen en pantalla.
4. Cada círculo acertado suma 10 puntos.
5. Tienes 30 segundos para conseguir la mayor puntuación posible.
6. Al finalizar, podrás ver tu puntuación, intentar superar tu récord o regresar al menú principal.

## ✨ Funcionalidades

- Interfaz gráfica con estilo arcade.
- Temporizador de 30 segundos.
- Objetivos que aparecen en posiciones aleatorias.
- Círculos de tamaños variables para aumentar el desafío.
- Dificultad progresiva según la puntuación.
- Sistema de puntuación de 10 puntos por acierto.
- Efecto visual de fuegos artificiales al acertar.
- Mensaje especial al conseguir un nuevo récord.
- Registro de la mejor puntuación durante la sesión.
- Opciones para volver a jugar o regresar al menú principal.

## 🛠️ Tecnologías utilizadas

- **Python 3:** lenguaje de programación principal.
- **Tkinter:** creación de la interfaz gráfica.
- **Random:** generación de posiciones, tamaños y colores aleatorios.
- **Math:** cálculo de las trayectorias de las partículas.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** control de versiones y publicación del proyecto.
- **Inteligencia artificial:** apoyo para generar, mejorar y revisar el código.

No se requieren librerías externas.

## 🚀 Instalación y ejecución

**Requisitos:** tener Python 3 instalado en el equipo.

Clona el repositorio:

```bash
git clone https://github.com/TU_USUARIO/reflex-challenge.git
```

Ingresa a la carpeta del proyecto:

```bash
cd reflex-challenge
```

Ejecuta el juego:

```bash
python main.py
```

**Nota:** reemplaza `TU_USUARIO` por tu nombre de usuario de GitHub.

## 🤖 Desarrollo asistido por inteligencia artificial

El proyecto se desarrolló mediante un proceso iterativo de vibecoding, utilizando inteligencia artificial como copiloto.

**Primera iteración:** creación de la estructura inicial del juego, interfaz, temporizador, objetivos y sistema de puntuación.

**Segunda iteración:** incorporación de dificultad progresiva, retroalimentación visual y mejoras en la pantalla de resultados.

**Tercera iteración:** implementación de fuegos artificiales localizados al acertar un objetivo.

**Ajuste adicional:** modificación del tamaño de los círculos para que varíe aleatoriamente y genere una experiencia menos predecible.

Cada cambio fue revisado mediante la ejecución del juego y pruebas manuales de sus funcionalidades.

## 🧪 Validación

Durante el desarrollo se realizaron pruebas manuales para comprobar:

- Inicio correcto de la aplicación.
- Funcionamiento del temporizador.
- Incremento de puntuación al acertar.
- Aparición de objetivos dentro del área de juego.
- Funcionamiento de los botones **PLAY AGAIN** y **MAIN MENU**.
- Conservación del récord entre partidas de una misma sesión.
- Visualización de las partículas y del indicador +10.
- Variación aleatoria del tamaño de los objetivos.

## 📌 Limitaciones

El récord se conserva únicamente mientras la aplicación permanece abierta. Al cerrar y volver a ejecutar el programa, la puntuación máxima se reinicia.

## 📚 Aprendizajes

Este proyecto permitió practicar la programación orientada a objetos, la creación de interfaces gráficas con Tkinter, la gestión de eventos y las animaciones mediante `after()`.

También permitió experimentar con el uso de inteligencia artificial para generar código, identificar oportunidades de mejora y desarrollar una aplicación funcional mediante instrucciones progresivamente más específicas.

## 👨‍💻 Autor

Kevin Salinas

Proyecto académico desarrollado para KODIGO.