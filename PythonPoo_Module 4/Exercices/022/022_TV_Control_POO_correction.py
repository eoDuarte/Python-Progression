from rich import print
from rich.panel import Panel


class RemoteControl:
    chanel_min: int = 1
    chanel_max: int = 5
    volum_min: int = 1
    volum_max: int = 5

    def __init__(self, chanel=1, volum=2):
        self.current_chanel: int = chanel
        self.volum_current: int = volum
        self.on: bool = False

    def on_off(self):
        self.on = not self.on

    def chanel_more(self):
        if self.on:
            if self.current_chanel == self.chanel_max:
                self.current_chanel = RemoteControl.chanel_min
            else:
                self.current_chanel += 1

    def chanel_less(self):
        if self.on:
            if self.current_chanel == self.chanel_min:
                self.current_chanel = RemoteControl.chanel_max
            else:
                self.current_chanel -= 1

    def volum_more(self):
        if self.on:
            if self.volum_current != self.volum_max:
                self.volum_current += 1

    def volum_less(self):
        if self.on:
            if self.volum_current != self.volum_min:
                self.volum_current -= 1

    def show_tv(self):

        content = ''
        if not self.on:
            content = f":prohibited: [red]The tv is off[/]"
        else:
            content = f"CHANEL ="
            for chanel in range(RemoteControl.chanel_min, RemoteControl.chanel_max + 1):
                if chanel == self.current_chanel:
                    content += f" [black on yellow] {chanel} [/]"
                else:
                    content += f" {chanel} "

            content += f"\nVOLUM  = "
            for volum in range(RemoteControl.volum_min, RemoteControl.volum_max + 1):
                if volum <= self.volum_current:
                    content += "[black on cyan] [/]"
                else:
                    content += "[black on white] [/]"

        tv = Panel(content, title=" [ TV ] ", width=30)
        print(tv)


c = RemoteControl(1, 1)
while True:
    c.show_tv()
    command =  str(input(f" < CH{c.current_chanel} >    - VOL{c.volum_current} +      "))
    match command:
        case '0':
            break
        case '@':
            c.on_off()
        case '>':
            c.chanel_more()
        case '<':
            c.chanel_less()
        case '-':
            c.volum_less()
        case '+':
             c.volum_more()
    print("\n" * 10)