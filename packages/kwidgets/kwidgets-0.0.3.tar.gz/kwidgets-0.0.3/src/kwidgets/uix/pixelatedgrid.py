from numpy import random
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line


class PixelatedGrid(Widget):
    background = ListProperty([0, 0, 0, 1])
    grid_color = ListProperty([47/255, 79/255, 79/255, 1])
    activated_color = ListProperty([0, 1, 0, 1])
    cell_length = NumericProperty(10)
    activated_cells = ObjectProperty(set())

    def __init__(self, **kwargs):
        super(PixelatedGrid, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.bind(activated_cells=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(*self.background)
            Rectangle(pos = [self.x,self.y], size=[self.width, self.height])
            Color(*self.grid_color)
            for x in range(0, int(self.width), self.cell_length):
                Line(points=[self.x + x, self.y, self.x + x, self.y + int(self.height)], width=1)
            for y in range(int(self.height), 0, -self.cell_length):
                Line(points=[self.x, self.y + y, self.x + int(self.width), self.y + y], width=1)
            Color(*self.activated_color)
            for x, y in self.activated_cells:
                Rectangle(pos=[self.x+x*self.cell_length, self.y+self.height-(y+1)*self.cell_length], size=[self.cell_length, self.cell_length])

    def visible_width(self):
        return self.width//self.cell_length

    def visible_height(self):
        return self.height//self.cell_length


class PixelatedGridApp(App):

    def activate_random(self, *args):
        num_cells=100
        visible_width = self.container.ids.thegrid.visible_width()
        visible_height = self.container.ids.thegrid.visible_height()
        self.container.ids.thegrid.activated_cells = set([(random.randint(0, visible_width), random.randint(0, visible_height)) for _ in range(0,num_cells)])

    def build(self):
        self.container = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    Button:
        size_hint: 1, None
        size: 0, 50
        text: 'Top Button'
    BoxLayout:
        orientation: 'horizontal'
        Button:
            size_hint: None, 1
            size: 50, 0
            text: 'L'
        PixelatedGrid:
            id: thegrid
        Button:
            size_hint: None, 1
            size: 50, 0
            text: 'R'
    Button:
        size_hint: 1, None
        size: 0, 50
        text: 'Bottom Button'
''')
        Clock.schedule_interval(self.activate_random, .5)
        return self.container


if __name__ == "__main__":
    PixelatedGridApp().run()
