#PARTE 3 DO TRABALHO
from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self._observers = []

    def anexar(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remover(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notificar(self):
        for observer in self._observers:
            observer.atualizar(self)

class Observer(ABC):
    @abstractmethod
    def atualizar(self, subject):
        pass