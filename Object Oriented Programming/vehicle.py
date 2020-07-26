from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    def stop(self):
        self.speed = 0
    
    @property
    @abstractmethod
    def speed():
        pass
    
    
print(Vehicle.mro())        
print(dir(Vehicle))