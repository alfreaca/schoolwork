class Animal:

    def __init__(self, growth_rate, food_need, water_need, name):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Embryo"
        self._type = "Generic"
        self._name = name

    def needs(self):
        return {'food need': self._food_need, 'water need': self._water_need}

    def report(self):
        return {'type': self._type, 'status': self._status, 'weight': self._weight, 'days growing': self._days_growing}

    def update_status(self):
        if self._weight > 15:
            self._status = "Old"
        elif self._weight > 10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Baby"
        elif self._weight == 0:
            self._status = "Embryo"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight +=  self._growth_rate

        self._days_growing += 1
        self.update_status()


def main():
    new_animal = Animal(1, 1, 1, 'Cow')
    print(new_animal.needs())
    print(new_animal.report())
    new_animal.grow(4, 4)
    print(new_animal.report())
    new_animal = Animal(1, 1, 1, 'Sheep')


main()