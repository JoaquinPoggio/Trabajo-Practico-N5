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
cola_personajes.encolar({'nombre': 'Luke Skywalker', 'planeta': 'Tatooine'})
cola_personajes.encolar({'nombre': 'Han Solo', 'planeta': 'Corellia'})
cola_personajes.encolar({'nombre': 'Leia', 'planeta': 'Alderaan'})
cola_personajes.encolar({'nombre': 'Yoda', 'planeta': 'Dagobah'})
cola_personajes.encolar({'nombre': 'Jar Jar Binks', 'planeta': 'Naboo'})
cola_personajes.encolar({'nombre': 'Darth Vader', 'planeta': 'Tatooine'})

def mostrar_pj_planeta(cola, planetas):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['planeta'] in planetas:
            print(f"{personaje['nombre']}")
        actual = actual.siguiente

def buscar_planeta_pj(cola, nombres):
    actual = cola.frente
    while actual:
        personaje = actual.dato
        if personaje['nombre'] in nombres:
            print(f"{personaje['nombre']} es del planeta {personaje['planeta']}")
        actual = actual.siguiente

def insertar_pj_antes_de_yoda(cola, nuevo_personaje, nombre_personaje):
    nueva_cola = Cola()
    personaje_insertado = False
    while not cola.vacia():
        personaje_actual = cola.desencolar()
        if personaje_actual['nombre'] == nombre_personaje and not personaje_insertado:
            nueva_cola.encolar(nuevo_personaje)
            personaje_insertado = True
        nueva_cola.encolar(personaje_actual)
    return nueva_cola

def eliminar_despues_de_pj(cola, nombre_personaje):
    nueva_cola = Cola()
    eliminar_siguiente = False
    while not cola.vacia():
        personaje_actual = cola.desencolar()
        if eliminar_siguiente:
            eliminar_siguiente = False
            continue
        nueva_cola.encolar(personaje_actual)
        if personaje_actual['nombre'] == nombre_personaje:
            eliminar_siguiente = True
    return nueva_cola

print("Personajes de Alderaan, Endor y Tatooine:")
mostrar_pj_planeta(cola_personajes, ['Alderaan', 'Endor', 'Tatooine'])

print("\nPlaneta natal de Luke Skywalker y Han Solo:")
buscar_planeta_pj(cola_personajes, ['Luke Skywalker', 'Han Solo'])

print("\nInsertar a Obi-Wan Kenobi antes de Yoda:")
nuevo_personaje = 'nombre' = 'Obi-Wan', 'planeta' = 'Stewjon'
cola_personajes = insertar_pj_antes_de_yoda(cola_personajes, nuevo_personaje, 'Yoda')
cola_personajes.recorrer()

print("\nEliminar el personaje ubicado después de Jar Jar Binks:")
cola_personajes = eliminar_despues_de_pj(cola_personajes, 'Jar Jar Binks')
cola_personajes.recorrer()
