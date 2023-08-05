from re import A


class Nota(object):
  def __init__(self):
    self.Control1 = Control1
    self.Control2 = Control2
    self.Proyecto = Proyecto
    self.Lab1 = Lab1
    self.Lab2 = Lab2
    self.Lab3 = Lab3
    Control1 = 1.0
    Control2 = 1.0
    Lab1 = 1.0
    Lab2 = 1.0
    Lab3 = 1.0
    Proyecto = 1.0

  def Evaluar(self,evaluacion,nota):
    if (evaluacion=='Control 1'):
      self.Control1==nota
    elif(evaluacion=='Control 2'):
      self.Control2==nota
    elif(evaluacion=='Laboratorio 1'):
      self.Lab1==nota
    elif(evaluacion=='Laboratorio 2'):
      self.Lab2==nota
    elif(evaluacion=='Laboratorio 3'):
      self.Lab3==nota
    elif(evaluacion=='Proyecto'):
      self.Proyecto==nota
    else:
      pass

  def calcularPromedio(self):
    prom= (self.Control1 + self.Control2 + self.Lab1 + self.Lab2 + self.Lab3 + self.Proyecto)/6
    print(prom)


class Alumno(object):
    def __init__(self,rut,nombre,apellido):
        self.rut=rut
        self.nombre=nombre
        self.apellido=apellido
        self.carrera=None
        self.nota=None
        self.promedio=None
    
    def EvaluarA(self,evaluacionu,notau=float):
        Nota.Evaluar(self,evaluacionu,notau)
    
    def calcularPromedio(self):
        self.promedio=Nota.calcularPromedio()
    
class Curso(object):
  def __init__(self,codigo,nombre,carrera=None):
    self.codigo=codigo
    self.nombre=nombre
    self.carrera=carrera
    self.estudiantes=[]

  def Buscaralumno(self,rut):
    for Alumno in self.estudiantes:
      if Alumno.rut==rut:
        return Alumno
    return None

  def Matricular(self,alumno):
    if(self.Buscaralumno(alumno.rut)==None):
      self.estudiantes.append(alumno)
    else:
      print('El estudiante no esta matriculado')
  
  def CerrarCurso(self):
    for alumno in self.estudiantes:
      alumno.calcularPromedio()
      print(alumno.rut,': Promedio ',alumno.Promedio)