import configparser
import json
import os
import random

from twisted.internet import reactor
from twisted.internet.task import LoopingCall
import pygame

FOLDER = 'blippi'

CONFIG = configparser.ConfigParser()
CONFIG.read(FOLDER + '/config.ini')

FPS = 15
# DISPLAY = pygame.display.set_mode((1900, 1080), pygame.FULLSCREEN)
DISPLAY = pygame.display.set_mode((1900, 1060))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAX_LIMIT = 90

J = [0, 1, 2, 3, 4, 7, 16, 19, 20, 21]
U = [0, 4, 5, 9, 10, 13, 14, 18, 19, 20, 21, 22, 23]
A = [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 18, 19, 23]
N = [0, 4, 5, 6, 9, 10, 12, 13, 14, 17, 18, 19, 23]


class Game:

    def __init__(self, gamer, numbers):
        self.gamer = gamer
        self.numbers = numbers
        self.finded = []
        self.indices = []
        self.faltan = list(self.numbers)
        self.faltan_J = list(map(lambda x: self.numbers[x], J))

    @property
    def puntaje(self):
        self.letras = ''
        if self.check_J():
            self.letras += 'J'
        if self.check_U():
            self.letras += 'U'
        if self.check_A():
            self.letras += 'A'
        if self.check_N():
            self.letras += 'N'
        return len(self.finded) + len(self.letras) * 25

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
            self.indices.append(self.numbers.index(n))
        if n in self.faltan_J:
            self.faltan_J.remove(n)
        return len(self.finded)

    def remove_number(self, n):
        if n in self.finded:
            self.finded.remove(n)
        return len(self.finded)

    def status(self):
        # faltan_list = self.faltan_J
        faltan_list = self.faltan
        nombre = (self.gamer + '                    ')[:20]
        faltan = ', '.join(str(x) for x in faltan_list[:4])
        if len(faltan_list) > 4:
            faltan += ', +'
        if len(faltan_list) > 0:
            return f'{nombre}: {len(self.finded)}  Letras: {self.letras}  Faltan: {faltan}'
        else:
            return f'{nombre}: {len(self.finded)}  Letras: {self.letras}  GANO'

    def check_J(self):
        for i in J:
            if i not in self.indices:
                return False
        return True

    def check_U(self):
        for i in U:
            if i not in self.indices:
                return False
        return True

    def check_A(self):
        for i in A:
            if i not in self.indices:
                return False
        return True

    def check_N(self):
        for i in N:
            if i not in self.indices:
                return False
        return True


class Screen:

    def __init__(self):
        self.background = json.loads(CONFIG['STYLES']['background'])
        self.opciones = []
        for i in range(MAX_LIMIT):
            self.opciones.append(i + 1)
        pygame.init()
        logo = pygame.image.load(os.path.join(f'{FOLDER}/logo.png'))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Bingo")
        self.imagen_grande = None
        self.escoger_button = Button(200, 900, 320, 80, 'Nuevo', color=json.loads(CONFIG['STYLES']['button']), size=50)
        self.escoger_button.set_callback(self.escoger)
        self.seleccionados = []
        backup = open(f'resultado/juego.bkp', 'r')
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
        for g in sorted(self.games, key=lambda x: x.puntaje):
            print(g.status())

    def seleccionado(self, number):
        self.imagen_grande = pygame.image.load(os.path.join(f'{FOLDER}/800PNG/{number}.png'))

    def display(self):
        self.process_events()
        # DISPLAY.fill(self.background)
        imagen = pygame.image.load(os.path.join(f'{FOLDER}/background.png'))
        background = pygame.transform.scale(imagen, (1900, 1060))
        DISPLAY.blit(background, (0, 0))

        imagen = pygame.image.load(os.path.join(f'{FOLDER}/panel.png'))
        background = pygame.transform.scale(imagen, (620, 620))
        DISPLAY.blit(background, (60, 220))

        imagen = pygame.image.load(os.path.join(f'{FOLDER}/header.png'))
        background = pygame.transform.scale(imagen, (668, 200))
        DISPLAY.blit(background, (20, 20))
        if self.imagen_grande:
            picture = pygame.transform.scale(self.imagen_grande, (500, 500))
            DISPLAY.blit(picture, (120, 280))
        x = 720
        y = 20
        for s in self.seleccionados:
            DISPLAY.blit(s, (x, y))
            x += 110
            if x > 1800:
                y += 110
                x = 720

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
        self.color_font = WHITE
        self.font = pygame.font.SysFont(CONFIG['STYLES']['font'], size)
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
        pygame.draw.rect(DISPLAY, self.color, self.rectangulo, border_radius=20)
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