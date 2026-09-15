class Node:

  __slots__ = ("__value","__next")

  def __init__(self,value):
    self.__value = value
    self.__next = None

  @property
  def value(self):
    return self.__value

  @property
  def next(self):
    return self.__next


  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise TypeError("El valor No debe ser None/Null.")
    self.__value = new_value

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next,Node):
      raise TypeError("El next de un nodo, solo puede ser None ó otro Nodo")
    self.__next = new_next


  def __str__(self):
    return str(self.__value)