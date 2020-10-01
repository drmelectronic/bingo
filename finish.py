import json
import os
import random

from twisted.internet import reactor
from twisted.internet.task import LoopingCall
import pygame

FOLDER = 'fallguys'

FPS = 15
# DISPLAY = pygame.display.set_mode((1900, 1080), pygame.FULLSCREEN)
DISPLAY = pygame.display.set_mode((1900, 1060))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:

    def __init__(self, gamer, numbers):
        self.gamer = gamer
        self.numbers = numbers
        self.finded = []
        self.faltan = list(self.numbers)

    def check(self, numbers):
        self.finded = []
        self.faltan = list(self.numbers)
        for n in numbers:
            self.check_number(n)
        return len(self.finded)

    def check_number(self, n):
        if n in self.numbers:
            self.finded.append(n)
            self.faltan.remove(n)
        return len(self.finded)

    def remove_number(self, n):
        if n in self.finded:
            self.finded.remove(n)
        return len(self.finded)

    def status(self):
        nombre = (self.gamer + '                    ')[:20]
        faltan = ', '.join(str(x) for x in self.faltan[:4])
        if len(faltan) > 4:
            faltan += ', +'
        return f'{nombre}: {len(self.finded)}    Faltan: {faltan}'


class Screen:

    def __init__(self):
        self.opciones = []
        for i in range(50):
            self.opciones.append(i + 1)
        pygame.init()
        logo = pygame.image.load(os.path.join(f'{FOLDER}/logo.png'))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Fall Guys Memory")
        self.imagen_grande = None
        self.escoger_button = Button(300, 900, 320, 80, 'ESCOGER', color=(255, 255, 100), size=50)
        self.escoger_button.set_callback(self.escoger)
        self.seleccionados = []
        backup = open(f'{FOLDER}/juego.bkp', 'r')
        js = json.loads(backup.read())
        backup.close()
        self.games = []
        for k, data in js.items():
            g = Game(k, data)
            self.games.append(g)

    def escoger(self):
        choice = random.choice(self.opciones)
        index = self.opciones.index(choice)
        self.opciones.pop(index)
        self.seleccionado(choice)
        imagen = pygame.image.load(os.path.join(f'{FOLDER}/100PNG/{choice}.png'))
        self.seleccionados.append(imagen)
        for g in self.games:
            g.check_number(choice)
        print('\n\n')
        for g in sorted(self.games, key=lambda x: -len(x.finded)):
            print(g.status())

    def seleccionado(self, number):
        self.imagen_grande = pygame.image.load(os.path.join(f'{FOLDER}/800PNG/{number}.png'))

    def display(self):
        self.process_events()
        DISPLAY.fill((190, 101, 154))
        if self.imagen_grande:
            DISPLAY.blit(self.imagen_grande, (50, 50))
        x = 900
        y = 50
        for s in self.seleccionados:
            DISPLAY.blit(s, (x, y))
            x += 120
            if x > 1800:
                y += 120
                x = 900

        self.escoger_button.display()
        pygame.display.flip()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.escoger_button.check_click(pos)


class Button:

    def __init__(self, x, y, w, h, texto, color, size):
        self.text = ''
        self.X = 0
        self.Y = 0
        self.args = []
        self.color_font = BLACK
        self.font = pygame.font.SysFont("Arial", size)
        self.is_clicked = False
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.texto = texto
        self.render()
        self.rectangulo = pygame.Rect(x, y, w, h)

    def set_callback(self, callback, *args):
        self.callback = callback
        self.args = args

    def clicked(self):
        self.callback(*self.args)

    def callback(self, *args):
        return

    def set_color_font(self, color):
        self.color_font = color
        self.render()

    def set_text(self, texto):
        self.texto = texto
        self.render()

    def render(self):
        self.text = self.font.render(self.texto, True, self.color_font)
        width = self.text.get_width()
        height = self.text.get_height()
        self.X = self.x - width / 2 + self.w / 2
        self.Y = self.y - height / 2 + self.h / 2

    def display(self):
        pygame.draw.rect(DISPLAY, self.color, self.rectangulo)
        DISPLAY.blit(self.text, (self.X, self.Y))

    def check_click(self, pos):
        if self.rectangulo.collidepoint(pos):
            self.clicked()


if __name__ == '__main__':
    screen = Screen()
    # winner = None
    # while winner is None:
    #     os.system('clear')
    #     for g in sorted(games, key=lambda x: -len(x.finded)):
    #         print(g.status())
    #     bolilla = input("SIGUIENTE BOLILLA: ")
    #     try:
    #         number = int(bolilla)
    #     except:
    #         continue
    #     else:
    #         for g in games:
    #             g.check_number(number)

    clock = LoopingCall(screen.display)
    clock.start(1 / FPS)
    reactor.run()