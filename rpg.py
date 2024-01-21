import random

class Jugador:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.nivel = 1
        self.vida = 100
        self.ataque = 0
        self.defensa = 0
        self.experiencia = 0
        self.establecer_clase()

    def mostrar_estado(self):
        print(f"{self.nombre} - {self.clase} - Nivel {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Experiencia: {self.experiencia}\n")

    def establecer_clase(self):
        if self.clase == "Caballero":
            self.ataque = 15
            self.defensa = 10
        elif self.clase == "Mago":
            self.ataque = 20
            self.defensa = 5
        elif self.clase == "Arquero":
            self.ataque = 10
            self.defensa = 7

    def atacar(self, enemigo):
        danio = max(0, self.ataque - enemigo.defensa)
        enemigo.vida -= danio
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {danio} de daño.")

    def subir_nivel(self):
        if self.experiencia >= self.nivel * 10:
            self.nivel += 1
            self.vida += 10
            self.ataque += 5
            self.defensa += 2
            self.experiencia = 0
            print(f"{self.nombre} ha subido de nivel!")
        else:
            print(f"{self.nombre} ha obtenido 10 de experiencia.\n")
            self.experiencia += 10

class Enemigo:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def mostrar_estado(self):
        print(f"{self.nombre} - Nivel 1")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}\n")

    def atacar(self, jugador):
        danio = max(0, self.ataque - jugador.defensa)
        jugador.vida -= danio
        print(f"{self.nombre} ataca a {jugador.nombre} y causa {danio} de daño.")    

# Función para la batalla
def batalla(jugador, enemigo):
    print(f"¡{jugador.nombre} entra en batalla contra {enemigo.nombre}!\n")

    while jugador.vida > 0 and enemigo.vida > 0:
        jugador.mostrar_estado()
        enemigo.mostrar_estado()

        # Turno del jugador
        input("Presiona Enter para atacar...")
        jugador.atacar(enemigo)

        # Verificar si el enemigo ha sido derrotado
        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ha sido derrotado!\n")
            jugador.experiencia += 10
            jugador.subir_nivel()
            break

        # Turno del enemigo
        enemigo.atacar(jugador)

        # Verificar si el jugador ha sido derrotado
        if jugador.vida <= 0:
            print(f"{jugador.nombre} ha sido derrotado. Fin del juego.")
            break

# Crear un jugador con selección de clase
nombre_jugador = input("Ingresa el nombre de tu personaje: ")
print("Selecciona tu clase: Caballero, Mago o Arquero")
clase_elegida = input("Clase: ")

# Validar la selección de clase
while clase_elegida not in ["Caballero", "Mago", "Arquero"]:
    print("Clase no válida. Por favor, selecciona Caballero, Mago o Arquero.")
    clase_elegida = input("Clase: ")

jugador_principal = Jugador(nombre_jugador, clase_elegida)

# Crear un enemigo
enemigo_1 = Enemigo("Ogro", 30, 8, 3)

# Comienza la batalla
batalla(jugador_principal, enemigo_1)





# Resto del código (Enemigo y la función de batalla) se mantiene igual



# Resto del código (crear enemigo, comenzar la batalla) se mantiene igual

