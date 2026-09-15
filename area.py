from queue import Queue

class Area:

  def __init__(self, nombre, capacidad_base):
    self.nombre = nombre
    self.capacidad_base = capacidad_base
    self.sobrecargada = False

    if nombre == "Recepción y Triaje":
      self.cola_alta = Queue()
      self.cola_normal = Queue()
    else:
      self.cola = Queue()

  def cantidad_solicitudes(self):
    if self.nombre == "Recepción y Triaje":
      return self.cola_alta.len() + self.cola_normal.len()
    else:
      return self.cola.len()

  def capacidad_actual(self):
    if self.nombre == "Recepción y Triaje":
      return self.capacidad_base

    if self.sobrecargada:
      capacidad = self.capacidad_base // 2

      if capacidad < 1:
        capacidad = 1

      return capacidad

    return self.capacidad_base