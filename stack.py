import random

from slinkedlist import slinkedlist

class Stack:

  def __init__(self):
    self.__s = slinkedlist()

  def __str__(self):
    result = [str(node.value) for node in self.__s]
    return ' || '.join(result)


  def push(self, e):
    self.__s.append(e)
    return True

  def pop(self):
    if not self.is_empty():
      e = self.__s.pop()
      return e
    else:
      raise ValueError("Error la pila esta vacia")

  def len(self):
    return self.__s.size

  def is_empty(self):
    return self.__s.size == 0

  def top(self):
    if not self.is_empty():
      return self.__s.tail.value

  def generate(self, num, min, max):
    for _ in range(num):
      self.push(random.randint(min,max))