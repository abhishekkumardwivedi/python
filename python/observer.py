import sys
from abc import abstractmethod, ABC
from __future__ import annotations
from typing import List


class Subject(ABC):
    """
    Manage subscribers
    """

    @abstractmethod
    def register(self, observer: Observer) -> None:
        """
        Register for listening events
        :return:
        """
        pass

    @abstractmethod
    def unregister(self, observer: Observer) -> None:
        """
        Unregister and stop listening events
        :return:
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Subject will notify each of the registered recipients
        :return:
        """
        pass


class ConcreteSubject(Subject):
    """
    Implementation of subject
    """

    _observers: List[Observer] = []

    def register(self, observer: Observer) -> None:
        self._observers.append(observer)
        pass

    def unregister(self, observer: Observer) -> None:
        self._observers.remove(observer)
        pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()
        pass


class Observer(ABC):
    """
    Observer interface
    """

    @abstractmethod
    def update(self) -> None:
        """
        Observers will implement this and get updates
        :return:
        """


class ObserverA(Observer):
    """
    Listen to change in subject
    """
    def update(self) -> None:
        print("ObserverA: Got update")


class ObserverB(Observer):
    """
    Listen to change in subject
    """
    def update(self) -> None:
        print("ObserverB: Got update")


if __name__ == "__main__":
    observerA = ObserverA
    observerB = ObserverB

    subject = ConcreteSubject
    subject.notify()
