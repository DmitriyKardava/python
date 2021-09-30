class Cell:
    def __init__(self, count):
        self.cell_count = count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count / other.cell_count)

    def __floordiv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, count):
        if count == 0:
            return ''
        _reversed = False
        if count < 0:
            _reversed = True
            count = -count
        for i in range(self.cell_count // count):
            print(f'*'*count)
        if self.cell_count - count*(self.cell_count // count) > 0:
            if _reversed:
                print(f' ' * (count - (self.cell_count - count * (self.cell_count // count))), end='')
            print(f'*' * (self.cell_count - count * (self.cell_count // count)))
        print()


cell1 = Cell(21)
cell2 = Cell(8)

print((cell1 + cell2).cell_count)
print((cell1 - cell2).cell_count)
print((cell1 * cell2).cell_count)
print((cell1 / cell2).cell_count)
print((cell1 // cell2).cell_count)
cell1.make_order(8)
cell1.make_order(-8)
cell2.make_order(3)
cell2.make_order(0)
cell2.make_order(100)
