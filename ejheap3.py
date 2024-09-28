import heapq

class Operacion:
    def __init__(self, encargado, descripcion, hora, prioridad, stormtroopers=None):
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.prioridad = prioridad
        self.stormtroopers = stormtroopers

    def __lt__(self, otra):
        return self.prioridad < otra.prioridad

    def __str__(self):
        return f"Encargado: {self.encargado}, Descripción: {self.descripcion}, Hora: {self.hora}, Prioridad: {self.prioridad}, Stormtroopers: {self.stormtroopers if self.stormtroopers else 'N/A'}"

class ColaPrioridad:
    def __init__(self):
        self.heap = []

    def agregar_operacion(self, operacion):
        heapq.heappush(self.heap, operacion)

    def atender_operacion(self):
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)
        else:
            return None

    def __len__(self):
        return len(self.heap)
    
def cargar_operaciones_iniciales(cola):
    cola.agregar_operacion(Operacion('Kylo Ren', 'Reparación de sable de luz', '10:00', 3))
    cola.agregar_operacion(Operacion('Snoke', 'Planificación del ataque a la Resistencia', '11:00', 3))
    
    cola.agregar_operacion(Operacion('Capitán Phasma', 'Entrenamiento de Stormtroopers', '09:00', 2, 100))
    cola.agregar_operacion(Operacion('Capitán Phasma', 'Inspección de armamento', '13:00', 2))
    cola.agregar_operacion(Operacion('Capitán Phasma', 'Vigilancia del hangar', '15:00', 2))
    cola.agregar_operacion(Operacion('Capitán Phasma', 'Revisión de seguridad en Sector 7', '17:00', 2))

    cola.agregar_operacion(Operacion('General Hux', 'Mantenimiento de la base Starkiller', '08:00', 1))
    cola.agregar_operacion(Operacion('General Hux', 'Control de suministros', '12:00', 1))
    cola.agregar_operacion(Operacion('General Hux', 'Planificación logística', '14:00', 1))
    cola.agregar_operacion(Operacion('General Hux', 'Revisión de informes', '16:00', 1))

def mostrar_operaciones_pendientes(cola):
    print("\nOperaciones pendientes:")
    for operacion in cola.heap:
        print(operacion)

def atender_operaciones(cola, num_atender):
    print("\nAtendiendo operaciones:")
    for _ in range(num_atender):
        operacion = cola.atender_operacion()
        if operacion:
            print(f"Atendiendo: {operacion}")
        else:
            print("No hay más operaciones para atender.")

def main():
    cola_operaciones = ColaPrioridad()
    cargar_operaciones_iniciales(cola_operaciones)
    mostrar_operaciones_pendientes(cola_operaciones)
    atender_operaciones(cola_operaciones, 5)

    print("\nAgregando operación del Capitán Phasma para revisión de intrusos en hangar B7")
    cola_operaciones.agregar_operacion(Operacion('Capitán Phasma', 'Revisión de intrusos en hangar B7', '18:00', 2, 25))

    atender_operaciones(cola_operaciones, 1)  # Atiende la sexta operación
    print("\nAgregando operación de Snoke para destruir el planeta Takodana")
    cola_operaciones.agregar_operacion(Operacion('Snoke', 'Destrucción del planeta Takodana', '19:00', 3))

    atender_operaciones(cola_operaciones, len(cola_operaciones))

if __name__ == "__main__":
    main()


