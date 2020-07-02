class Cell():
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        if isinstance(other, Cell):
            return self.num + other.num

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.num - other.num >= 0:
                return self.num - other.num

    def __mul__(self, other):
        if isinstance(other, Cell):
            new_cell = Cell(self.num * other.num)
            return new_cell

    def __truediv__(self, other):
        if isinstance(other, Cell):
            new_cell = Cell(self.num // other.num)
            return new_cell

    def make_order(self, unit):
        left = self.num
        my_str = ''
        while left - unit > 0:
            my_str += '*' * unit
            my_str += '\n'
            left -= unit
        my_str += '*' * left
        print(my_str)


cell_1 = Cell(20)
cell_2 = Cell(10)
print('cell_1:', cell_1.num, 'cell_2:', cell_2.num)

print('\ncell_2 + cell_1 = ', cell_2 + cell_1)
print('\ncell_2 - cell_1 = ', cell_1 - cell_2)
print('\ncell_1 * cell_2:')
cell_3 = cell_1 * cell_2
cell_3.make_order(10)
cell_3 = cell_1 / cell_2
print('\ncell_1 / cell_2:')
cell_3.make_order(10)



