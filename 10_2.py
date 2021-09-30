from abc import ABC, abstractmethod


class Clothes(ABC):
    instances = []

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.name = 'пальто'
        self.__class__.instances.append(self)

    @property
    def cloth_consumption(self):
        return self.size/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        self.name = 'костюм'
        self.__class__.instances.append(self)

    @property
    def cloth_consumption(self):
        return self.height*2 + 0.3


coat1 = Coat(50)
print(f"Расход ткани на {coat1.name}: {coat1.cloth_consumption}")
costume1 = Costume(160)
print(f"Расход ткани на {costume1.name}: {costume1.cloth_consumption}")
total_cloth_consumption = 0
for wear in Clothes.instances:
    total_cloth_consumption += wear.cloth_consumption
print(f"Общий расход ткани: {total_cloth_consumption}")
