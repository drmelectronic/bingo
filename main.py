import json
import random

from fpdf import FPDF


class Bingo(FPDF):

    def __init__(self):
        super().__init__()

    def create_page(self, game):
        self.add_page()
        # self.line(5, 5, 205, 5)
        # self.line(5, 292, 205, 292)
        # self.line(5, 5, 5, 292)
        # self.line(205, 5, 205, 292)

        self.set_xy(0, 22)
        self.image('template.png', w=200, h=250)

        self.set_font('Arial', 'B', 50)
        self.set_text_color(100, 100, 100)
        x = 23.5
        for i in range(5):
            y = 98
            for j in range(5):
                number = game.columnas[j][i]
                if number is not None:
                    if number < 10:
                        self.text(x + 5, y, str(number))
                    else:
                        self.text(x, y, str(number))
                y += 37
            x += 34.7
        self.set_font('Arial', 'B', 20)
        self.text(30, 280, game.gamer)


class Game:

    def __init__(self):
        self.gamer = None
        self.numbers = []
        self.columnas = []
        for i in range(5):
            fila = []
            for j in range(5):
                if i == j == 2:
                    number = None
                else:
                    number = self.new_number(j)
                fila.append(number)
            self.columnas.append(fila)

    def set_gamer(self, gamer):
        self.gamer = gamer

    def new_number(self, col):
        min_limit = 1 + col * 10
        max_limit = 10 + col * 10
        number = random.randint(min_limit, max_limit)
        while number in self.numbers:
            number = random.randint(min_limit, max_limit)
        self.numbers.append(number)
        return number

    def __eq__(self, other):
        for i in range(51):
            if i in self.numbers and i not in other.numbers:
                return False
            if i not in self.numbers and i in other.numbers:
                return False
        return self.numbers == other.numbers


if __name__ == '__main__':
    games = []

    niños = [
        'Jesús',
        'André',
        'Akira',
        '01', '02', '03'
    ]

    while len(niños):
        game = Game()
        repetido = False
        for g in games:
            if g == game:
                repetido = True
        if not repetido:
            game.set_gamer(niños.pop())
            games.append(game)
    js = {}
    for g in games:
        pdf = Bingo()
        pdf.create_page(g)
        js[g.gamer] = g.numbers
        pdf.output(f'{g.gamer}.pdf', 'F')
    backup = open('juego.bkp', 'w')
    backup.write(json.dumps(js, indent=4))
    backup.close()
