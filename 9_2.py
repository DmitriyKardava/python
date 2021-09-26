class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._width = _width
        self._length = _length

    def calc_mass(self):
        return self._length * self._width * 25 * 5 / 1000


my_road = Road(_length=5000, _width=20)
print(f"Масса асфальта: {my_road.calc_mass()} тонн")
