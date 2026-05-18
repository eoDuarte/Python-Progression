from rich import print
from rich.panel import Panel
from rich import inspect

class gamer:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.favorites = list()


    def add_favorites(self, game):
        self.favorites.append(game)
        self.favorites = sorted(self.favorites, key=str.lower)

    def information(self):
        content = f"Real name: [black on blue]{self.name} [/]"
        content += f"\nFavortes games: "
        for num, game in enumerate(self.favorites):
            content += f"\n:video_game: [blue]{game}[/]"
        panel = Panel(content, title=f"Gamer <{self.nick}>", width= 50)
        print(panel)




j1 = gamer("fabricio da silva", "detonator 2025")
j1.add_favorites("mario bross")
j1.add_favorites("call of duty")
#inspect(j1)
j1.information()

j2 = gamer ("patricia correia", "pitty pink")
j2.add_favorites("it take too")
j2.add_favorites("fast and furius")
j2.information()