__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer interface that defines the update method.
    """
    @abstractmethod
    def update(self, message: str):
        """
        Receive an update from the subject.
        """
        pass