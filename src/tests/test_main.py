import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import Tarea,AdministradorDeTareas,tarea1
import unittest
from datetime import datetime

import io

#Test tarea creada
'''def test_create_task():
    myTask = Task('Task1')
    print(myTask.nameTag)

if __name__ == "__main__":
    test_create_task()

#Test tarea completada s
def test_complete_task():
    myTask = Task('Completed')
    myTask.complete()
    assert myTask.completed == True
    print(myTask.completed)

'''
# if __name__ == "__main__": 
#     test_complete_task()

class TestTaskManager(unittest.TestCase):
    def test_creacion_tarea(self):
        print(tarea1.nombreEtiqueta)
        #Compara dos valores y verifica que sean iguales
        self.assertEqual(tarea1.nombreEtiqueta, 1)
        self.assertEqual(tarea1.descripcion, "Aprender Python")
        self.assertEqual(tarea1.prioridad, "A")
        self.assertEqual(tarea1.fecha_vencimiento, datetime(2024, 6, 10))
        #Verifica si es Falsa
        self.assertTrue(tarea1.completada)

    def test_creacion_tarea_prioridad_invalida(self):
        #Verifica si lanza una excepcion
        with self.assertRaises(ValueError):
            Tarea("Aprender Python", "Descripción", "D")

    def test_creacion_tarea_fecha_invalida(self):
        with self.assertRaises(ValueError):
            Tarea("Aprender Python", "Descripción", "A", "fecha_invalida")

    def test_completar_tarea(self):
        tarea = Tarea("Aprender Python")
        tarea.completar()
        self.assertTrue(tarea.completada)

    def test_eliminar_tarea(self):
        administrador = AdministradorDeTareas()
        tarea = Tarea("Aprender Python")
        tarea.completar()
        administrador.añadir_tarea(tarea)
        administrador.eliminar_tarea(tarea)
        self.assertNotIn(tarea, administrador.tareas)


        

if __name__ == '__main__':
    #unittest.main() #Si no queremos el mensaje personzalizado
    #Cada funcion, se toma como una prueba, sin importar que tenga mas de un test dentro

    stream = io.StringIO() #Flujo en memoria para hacer el mensaje personalizado
    runner = unittest.TextTestRunner(stream=stream) 
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTaskManager) #Carga todas las pruebas utilizando el cargador de pruebas unitarias 
    result = runner.run(suite)

    
    print("RESULTADOS DE LAS PRUEBAS:")
    print("Número de pruebas ejecutadas:", result.testsRun)
    if result.wasSuccessful():
        print("Todas las pruebas pasaron exitosamente!")
    else:
        print("Algunas pruebas fallaron.")
        print("Número de fallos:", len(result.failures))
        print("Número de errores:", len(result.errors))

    
    # Imprimir los detalles de los fallos y errores
    if result.failures:
        print("\nFallos:")
        for failure in result.failures:
            print(failure[1])
    
    if result.errors:
        print("\nErrores:")
        for error in result.errors:
            print(error[1])
