from abc import ABC, abstractmethod


# Passenger & Cargo Carriers
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# Military & Commercial Planes
class Plane(ABC):
    def __init__(self, carrier: Carrier):
        self.carrier = carrier

    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


class RefinedCarrier(Carrier):
    # Реализация абстрактных методов
    def carry_military(self, items: str) -> str:
        print(f'i`m carry_militaries define with value: {items}')

    def carry_commercial(self, items: str) -> str:
        print(f'i`m carry_commercial define with value: {items}')


class RefinedPlane(Plane):
    # Инициализация магического и реализация абстрактных методов
    def __init__(self, carrier: Carrier, items):
        super().__init__(carrier)
        self.items = items

    def display_description(self) -> str:
        print(f'i`m display_description define')

    def add_objects(self, new_objects: str) -> str:
        self.carrier.carry_military(new_objects)
        self.carrier.carry_commercial('some commercial staff')
        print(f'i`m add_objects define with value: {new_objects}')


ref_car = RefinedCarrier()

plane1 = RefinedPlane(ref_car, 'some object1')
plane2 = RefinedPlane(ref_car, 'some object2')

plane1.display_description()
plane2.display_description()
print()
plane1.carrier.carry_military('any obj')
plane2.carrier.carry_commercial('any obj')
print()
plane1.add_objects('new_obj_plane1')
plane2.add_objects('new_obj_plane2')
