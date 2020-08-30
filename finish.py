import json
import os


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


if __name__ == '__main__':
    backup = open('juego1.bkp', 'r')
    js = json.loads(backup.read())
    backup.close()
    games = []
    for k, data in js.items():
        g = Game(k, data)
        games.append(g)
    winner = None
    while winner is None:
        os.system('clear')
        for g in sorted(games, key=lambda x: -len(x.finded)):
            print(g.status())
        bolilla = input("SIGUIENTE BOLILLA: ")
        try:
            number = int(bolilla)
        except:
            continue
        else:
            for g in games:
                g.check_number(number)
