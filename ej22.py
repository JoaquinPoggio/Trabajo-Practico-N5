class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.fondo = None

    def vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.vacia():
            self.frente = nuevo_nodo
        else:
            self.fondo.siguiente = nuevo_nodo
        self.fondo = nuevo_nodo

    def desencolar(self):
        if not self.vacia():
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.fondo = None
            return dato
        else:
            return None

    def recorrer(self):
        actual = self.frente
        while actual:
            print(actual.dato)
            actual = actual.siguiente

cola_personajes = Cola()
cola_personajes.encolar({'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
cola_personajes.encolar({'nombre': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'})
cola_personajes.encolar({'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
cola_personajes.encolar({'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})
cola_personajes.encolar({'nombre': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'})
cola_personajes.encolar({'nombre': 'Bruce Banner', 'superheroe': 'Hulk', 'genero': 'M'})

def buscar_pj_superheroe(cola, nombre_superheroe):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['superheroe'] == nombre_superheroe:
            print(f"El nombre del personaje de {nombre_superheroe} es {personaje['nombre']}")
        actual = actual.siguiente

def mostrar_superheroes_femeninos(cola):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['genero'] == 'F':
            print(f"{personaje['superheroe']}")
        actual = actual.siguiente

def mostrar_pj_masculinos(cola):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['genero'] == 'M':
            print(f"{personaje['nombre']}")
        actual = actual.siguiente

def buscar_superheroe_pj(cola, nombre_personaje):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['nombre'] == nombre_personaje:
            print(f"El nombre del superhéroe de {nombre_personaje} es {personaje['superheroe']}")
        actual = actual.siguiente

def mostrar_datos_con_s(cola):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['nombre'].startswith('S') or personaje['superheroe'].startswith('S'):
            print(personaje)
        actual = actual.siguiente

def buscar_carol_danvers(cola):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['nombre'] == 'Carol Danvers':
            print(f"Carol Danvers se encuentra en la cola y su nombre de superheroe es {personaje['superheroe']}")
            return
        actual = actual.siguiente
    print("Carol Danvers no se encuentra en la cola.")


print("Nombre del personaje de Capitana Marvel:")
buscar_pj_superheroe(cola_personajes, 'Capitana Marvel')

print("\n Superhéroes femeninos:")
mostrar_superheroes_femeninos(cola_personajes)

print("\n Personajes masculinos:")
mostrar_pj_masculinos(cola_personajes)

print("\n Superhéroe de Scott Lang:")
buscar_superheroe_pj(cola_personajes, 'Scott Lang')

print("\n Personajes o superhéroes cuyos nombres comienzan con 'S':")
mostrar_datos_con_s(cola_personajes)

print("\n ¿Carol Danvers está en la cola?")
buscar_carol_danvers(cola_personajes)