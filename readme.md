# EXPLICACIÓN

### Nombre: Juan Fernando Rosero
### Fecha de entrega: 13-05-2025

## ¿Cómo funciona?

Ingreso de jugadores:
El usuario ingresa una cantidad par de jugadores desde la consola. Cada jugador recibe un nivel de habilidad aleatorio (skill entre 1 y 100).

Emparejamiento:
El sistema utiliza una cola (Queue) para emparejar jugadores disponibles en cada ronda. (Es el mismo sistema que se emplea en la mayoría de videojuegos actualmente, agrega varios jugadores a una cola (que en muchos juegos, depende de las estadísticas de rendimiento o MMR) y cuando la cola llega a un número establecido de jugadores, el match empieza).

Rondas y estructura:
Se ejecutan rondas eliminatorias hasta que queda un solo campeón. Al finalizar, se imprime el historial de victorias y se guarda el campeón en un archivo champion.json.
## NOTA: El archivo champion.json se crea en la carpeta donde se ejecuta el programa. La lista se limpia tras cada enfrentamiento (por falta de tiempo para evitar consultas por ID de usuario).

## Consulta posterior:
El usuario puede consultar el campeón desde el menú.

## Estructuras de datos implementadas:

Carpeta: structures.
Requisito	Implementación	Uso
Pilas (Stack)	stack.py	Almacena las victorias de cada jugador
Colas (Queue)	queue.py	Emparejamiento de jugadores disponibles
Array por nivel	Tournament.rounds	Guarda las rondas del torneo por nivel
Lista circular doble	double_circular_list.py	Navegación de todos los matches registrados
Lista simple	singly_linked_list.py	Historial de eventos de cada jugador
Lista doble	doubly_linked_list.py	Registro de enfrentamientos directos

## Estructura del sistema:

Carpeta: system.
Player: Clase que representa a un jugador con nombre, skill, eventos y victorias.
Match: Lógica para enfrentar dos jugadores.
Tournament: Controla el torneo y usa todas las estructuras.
TournamentManager: Interfaz de menú e interacción con el usuario.

## Para ejecutar, se escribe en la consola (desde la raíz) `python main.py` y posteriormente, se escribe lo del menú según quiera. (para empezar el torneo se requiere mínimo 2 players).

Eso es todo profe.