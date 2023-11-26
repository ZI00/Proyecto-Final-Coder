from django.test import TestCase

from control_estudios.models import Curso
# Create your tests here.
class CursoTest(TestCase):
    
    def test_creacion_curso(self):
        curso = Curso(nombre="titulo", comision=100)
        curso.save()

        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(curso.nombre, "titulo")
        self.assertEqual(curso.comision, 100)
        
    def test_curso_str(self):
        curso = Curso(nombre="Terminator", comision=30)
        curso.save()
        
        self.assertEqual(curso.__str__(), "Terminator (30)")