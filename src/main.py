from datetime import datetime

# Constructor, inicializa una lista vacía llamada "tasks" para almacenar tareas
class AdministradorDeTareas:
    def __init__(self):
        self.tareas = []

    # Método que toma una tarea como argumento y la añade a la lista tareas
    def añadir_tarea(self, tarea):
        self.tareas.append(tarea)

    # Método que toma una tarea (tarea) como argumento e intenta eliminarla de la lista tareas.
    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            if tarea.completada:
                self.tareas.remove(tarea)
            else:
                raise ValueError("La tarea no está completada")
        else:
            raise ValueError("Tarea no encontrada")

    # Método que toma una tarea, si está en la lista llama a completar para marcarla como completa, si no lanza un mensaje de error
    def completar_tarea(self, tarea):
        if tarea in self.tareas:
            tarea.completar()
        else:
            raise ValueError("Tarea no encontrada")
        
    # Método para mostrar las tareas de la lista, las enumera
    def obtener_tareas(self):
        for idx, tarea in enumerate(self.tareas, start=1):
            info_tarea = f"Tarea {idx}: {tarea.descripcion}, Completada: {tarea.completada}"
            if hasattr(tarea, 'fecha_vencimiento'):
                info_tarea += f", Fecha de vencimiento: {tarea.fecha_vencimiento}"
            print(info_tarea)

# Constructor de la clase Tarea, se llama cuando se crea una instancia de Tarea
# Inicializa todos los atributos de la tarea
class Tarea:
    def __init__(self, nombreEtiqueta, descripcion=None, prioridad=None, fecha_vencimiento=None):
        self.nombreEtiqueta = nombreEtiqueta
        self.descripcion = descripcion
        self.prioridad = prioridad
        if self.prioridad is not None and prioridad not in ['A', 'B', 'C']:
            raise ValueError("La prioridad debe ser: A, B o C")
        if fecha_vencimiento is not None:  # Verificar si fecha_vencimiento se proporcionó
            self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        else:
            self.fecha_vencimiento = None
        self.completada = False
        print('Tarea creada')

    def completar(self):
        self.completada = True


# Crear instancia de AdministradorDeTareas
administrador_de_tareas = AdministradorDeTareas()

# Crear instancias de Tarea
tarea1 = Tarea(1, "Aprender Python", "A", "2024-06-10")
tarea2 = Tarea(2, "Aprender Java", "B", "2024-06-08")

# Añadir la tarea al AdministradorDeTareas
administrador_de_tareas.añadir_tarea(tarea1)
administrador_de_tareas.añadir_tarea(tarea2)

# Completar la tarea
administrador_de_tareas.completar_tarea(tarea1)

# Marcar la tarea como completa
tarea1.completar()

# Traer la lista de tareas 
administrador_de_tareas.obtener_tareas()
