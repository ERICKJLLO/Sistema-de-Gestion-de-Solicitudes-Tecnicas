from stack import Stack
from area import Area


class Sistema:

  def __init__(self):
    self.areas = Stack()
    self.turno = 0

    self.areas.push(Area("Control de Calidad y Cierre", 1))
    self.areas.push(Area("Reparación / Corrección", 2))
    self.areas.push(Area("Diagnóstico Técnico", 2))
    self.areas.push(Area("Recepción y Triaje", 4))

  def obtener_area_superior(self):
    return self.areas.top()

  def registrar_solicitud(self, solicitud):
    area = self.obtener_area_superior()

    if area.nombre == "Recepción y Triaje":
      if solicitud.prioridad == "Alta":
        area.cola_alta.enqueue(solicitud)
      else:
        area.cola_normal.enqueue(solicitud)
    else:
      area.cola.enqueue(solicitud)

  def preparar_turno(self):
    temporal = Stack()

    while not self.areas.is_empty():
      area = self.areas.pop()

      area.pendientes_inicio_turno = area.cantidad_solicitudes()

      if area.nombre == "Recepción y Triaje":
        area.sobrecargada = False
      elif area.pendientes_inicio_turno > 5:
        area.sobrecargada = True
      else:
        area.sobrecargada = False

      temporal.push(area)

    while not temporal.is_empty():
      self.areas.push(temporal.pop())

  def ejecutar_turno(self):
    if self.sistema_vacio():
      print("No hay solicitudes pendientes.")
      return

    self.turno += 1
    self.preparar_turno()

    procesadas = Stack()

    while not self.areas.is_empty():

      area = self.areas.pop()
      procesadas.push(area)

      cantidad = area.pendientes_inicio_turno
      capacidad = area.capacidad_actual()

      cantidad_procesar = cantidad

      if cantidad_procesar > capacidad:
        cantidad_procesar = capacidad

      if area.sobrecargada:
        print("ALERTA: Área sobrecargada:", area.nombre)
        print("Capacidad efectiva:", capacidad)

      if area.nombre == "Recepción y Triaje":

        for _ in range(cantidad_procesar):

          if not area.cola_alta.is_empty():
            solicitud = area.cola_alta.dequeue()
          elif not area.cola_normal.is_empty():
            solicitud = area.cola_normal.dequeue()
          else:
            break

          print("Procesada:", solicitud.id, "-", area.nombre)

          self.transferir_solicitud(solicitud)

      else:

        for _ in range(cantidad_procesar):

          if area.cola.is_empty():
            break

          solicitud = area.cola.dequeue()

          print("Procesada:", solicitud.id, "-", area.nombre)

          self.transferir_solicitud(solicitud)

    while not procesadas.is_empty():
      self.areas.push(procesadas.pop())

    print("Turno", self.turno, "finalizado.")

  def transferir_solicitud(self, solicitud):

    if self.areas.is_empty():
      print("Solicitud", solicitud.id, "completó el proceso.")
      return

    siguiente_area = self.areas.top()

    if siguiente_area.nombre == "Recepción y Triaje":

      if solicitud.prioridad == "Alta":
        siguiente_area.cola_alta.enqueue(solicitud)
      else:
        siguiente_area.cola_normal.enqueue(solicitud)

    else:
      siguiente_area.cola.enqueue(solicitud)

    print("Transferida:", solicitud.id, "->", siguiente_area.nombre)

  def sistema_vacio(self):
    temporal = Stack()
    vacio = True

    while not self.areas.is_empty():

      area = self.areas.pop()

      if area.cantidad_solicitudes() > 0:
        vacio = False

      temporal.push(area)

    while not temporal.is_empty():
      self.areas.push(temporal.pop())

    return vacio

  def mostrar_estado(self):
    temporal = Stack()

    print()
    print("ESTADO DEL SISTEMA")
    print("Turno:", self.turno)

    while not self.areas.is_empty():

      area = self.areas.pop()
      temporal.push(area)

    while not temporal.is_empty():

      area = temporal.pop()

      print()
      print("Área:", area.nombre)
      print("Capacidad:", area.capacidad_base)
      print("Pendientes:", area.cantidad_solicitudes())

      if area.nombre == "Recepción y Triaje":
        print("Cola Alta:", area.cola_alta)
        print("Cola Normal:", area.cola_normal)
      else:
        print("Cola:", area.cola)

      self.areas.push(area)

  def eliminar_area(self, nombre):
    temporal = Stack()
    eliminada = None

    while not self.areas.is_empty():

      area = self.areas.pop()

      if area.nombre == nombre:
        eliminada = area
        break

      temporal.push(area)

    if eliminada is None:

      while not temporal.is_empty():
        self.areas.push(temporal.pop())

      return False

    if self.areas.is_empty():

      self.areas.push(eliminada)

      while not temporal.is_empty():
        self.areas.push(temporal.pop())

      return False

    destino = self.areas.top()

    if eliminada.nombre == "Recepción y Triaje":

      while not eliminada.cola_alta.is_empty():

        solicitud = eliminada.cola_alta.dequeue()

        if destino.nombre == "Recepción y Triaje":
          destino.cola_alta.enqueue(solicitud)
        else:
          destino.cola.enqueue(solicitud)

      while not eliminada.cola_normal.is_empty():

        solicitud = eliminada.cola_normal.dequeue()

        if destino.nombre == "Recepción y Triaje":
          destino.cola_normal.enqueue(solicitud)
        else:
          destino.cola.enqueue(solicitud)

    else:

      while not eliminada.cola.is_empty():

        solicitud = eliminada.cola.dequeue()

        if destino.nombre == "Recepción y Triaje":

          if solicitud.prioridad == "Alta":
            destino.cola_alta.enqueue(solicitud)
          else:
            destino.cola_normal.enqueue(solicitud)

        else:
          destino.cola.enqueue(solicitud)

    while not temporal.is_empty():
      self.areas.push(temporal.pop())

    print("Área eliminada:", eliminada.nombre)
    print("Solicitudes redistribuidas a:", destino.nombre)

    return True

  def agregar_area(self, nombre, capacidad):
    nueva_area = Area(nombre, capacidad)
    self.areas.push(nueva_area)

    print("Área agregada:", nombre)

  def ejecutar_automaticamente(self):
    while not self.sistema_vacio():
      self.ejecutar_turno()