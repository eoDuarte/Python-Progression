#Create a class called remote control, where we will simulate the operation
#simple control (on/off, volume and channel)
from rich import print


class constrol:
    def __init__(self, on_off = int(input("The TV is off, To on tv press [1]: "))):
        self.on_off = on_off
        while self.on_off!= 1:

            if on_off != 1:
                print("The TV is off, To on tv press [1]: ")

            else:
                print(f"The tv is on | [blues]CHANNEL 1[/] ")


    def change_channel(self):
        count = 1
        while count != 0:
            chennel = int(input("CHANNEL | 8 = ↑ and 2 = ↓ : "))
            if chennel == 8:
                count += 1
                print(f"[blue]CHANNEL{count}[/]")

            if chennel == 2:
                count -= 1
                print(f"[blue]CHANNEL{count}[/]")

            if chennel == 0:
                break
        if count == 0:
            print("[red]The TV is off[/]")

    def volume(self):
        vol = 1
        while vol != 0:
            volumeup = int(input(f"VOLUME |  6 = + and - = 4"
                                 f"\n: "))
            if volumeup == 6:
                vol += 2
                print(f"[green]- Volume + {vol}[/]")
            if volumeup == 4:
                vol -= 2
                print(f"[green]- Volume + {vol}[/]")

            if volumeup == 0:
                break


user1 = constrol()

user1.change_channel()

user1.volume()
