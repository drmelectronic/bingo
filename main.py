import json
import random

from fpdf import FPDF

FOLDER = 'tcontur'
MAX_LIMIT = 90


class Bingo(FPDF):

    def __init__(self):
        super().__init__()

    def create_page(self, game):
        print('Creando pdf', g.gamer)
        self.add_page()
        # self.line(5, 5, 205, 5)
        # self.line(5, 292, 205, 292)
        # self.line(5, 5, 5, 292)
        # self.line(205, 5, 205, 292)

        self.set_xy(0, 22)
        self.image(f'{FOLDER}/template.png', w=200, x=5, y=25)

        self.set_font('Arial', 'B', 50)
        self.set_text_color(255, 255, 255)
        x = 27.5
        for i in range(5):
            y = 102
            for j in range(5):
                number = game.columnas[j][i]
                if number is not None:
                    self.set_xy(x - 8, y - 24)
                    self.image(f'{FOLDER}/100PNG/{number}.png', w=30, h=30)
                    # if number < 10:
                    #     self.text(x + 5, y, str(number))
                    # else:
                    #     self.text(x, y, str(number))
                y += 36.35
            x += 35.5
        # self.set_text_color(40, 40, 40)  # black
        self.set_text_color(40, 40, 40)  # white
        self.set_font('Arial', 'B', 20)
        self.text(20, 268, 'Jugador: ' + game.gamer)


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
        # return 1
        per_column = MAX_LIMIT / 5
        min_limit = int(1 + col * per_column)
        max_limit = int(per_column + col * per_column)
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
        'Polito',
        'Lupe',
        'Francesca',
        'Daniel',
        'Pamela',
        'Yuyo',
        'Yiya',
        'Joe',
        'Roxana',
        'Robert',
        'Geraldine',
        'Ronald',
        'Tim',
        'Camila',
        'Carmen',
        'Christian',
        'Luis Alonso',
        'Juan Diego',
        'Jenny',
        'César',
        'Doris',
        'Rosa',
        'Francisco',
        'Andrea',
        'Jeremy',
        'Jonathan',
        'Brisa',
        'Ricardo',
        'Giuliana',
        'Deisy',
        'Tía Mimba',
        'Meddly',
        'Juan',
        'Esteban',
        'Milán',
        'Mateo',
        'David',
        'Josué',
        'César',
        'Cayetana',
        'Damaris',
        'Loana',
        'Abigail',
    ]
    niños = [str(i).zfill(2) for i in range(1, 40)]

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
        pdf.output(f'resultado/tarjetas/{g.gamer}.pdf')
    backup = open(f'resultado/juego.bkp', 'w')
    backup.write(json.dumps(js, indent=4))
    backup.close()
