'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    title = 'thing'

    def draw(self):
        print('Stationary Drawing')


class Pen(Stationery):
    def draw(self):
        print('Pen Drawing')


class Pencil(Stationery):
    def draw(self):
        print('Pencil Drawing')


class Handle(Stationery):
    def draw(self):
        print('Handle Drawing')


my_st = Stationery()
print('Stationary')
my_st.draw()

my_pen = Pen()
print('Pen')
my_pen.draw()

my_pencil = Pencil()
print('Pencil')
my_pencil.draw()

my_handle = Handle()
print('Handle')
my_handle.draw()

a = 2 + 2