class Solicitud:

  def __init__(self, id, descripcion, prioridad):
    self.id = id
    self.descripcion = descripcion
    self.prioridad = prioridad

  def __str__(self):
    return self.id