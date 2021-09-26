class Stationery:
    title = ''

    def draw(self):
        if self.title:
            print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    title = 'ручка'


class Pencil(Stationery):
    title = 'карандаш'


class Handle(Stationery):
    title = 'маркер'


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
