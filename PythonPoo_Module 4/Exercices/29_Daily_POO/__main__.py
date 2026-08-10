from daily import Daily
from rich import print
def main():
    d = Daily("leo")
    d.write("Abobrinha")
    d.write("Canela")
    d.read("leo")

if __name__ == "__main__":
    main()