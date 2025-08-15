__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from typing import List
from patterns.observer.observer import Observer


class Subject(ABC):
    """
    Subject class that maintains a list of observers and notifies them of changes.
    """
    @abstractmethod
    def update(self, message: str):
        """
        Receive an update from the subject.
        """
        pass

    def __init__(self):
        """
        Initialize the class attribute to an empty list.
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer):
        """
        Add an observer to the list.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """
        Remove an observer from the list.
        """
        pass
    
    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Notify all observers with a message.
        """
        pass
            
        

