import random

from slinkedlist import slinkedlist

class Queue:

  def __init__(self):
    self.__q = slinkedlist()

  def __str__(self):
    result = [str(node.value) for node in self.__q]
    return ' -- '.join(result)


  def enqueue(self, e):
    self.__q.append(e)
    return True

  def dequeue(self):
    if not self.is_empty():
      e = self.__q.popfirst()
      return e
    else:
      raise ValueError("Error la cola esta vacia")

  def len(self):
    return self.__q.size

  def is_empty(self):
    return self.__q.size == 0

  def first(self):
    if not self.is_empty():
      return self.__q.getvaluebyindex(0)


  def generate(self, num, min, max):
    for _ in range(num):
      self.enqueue(random.randint(min,max))