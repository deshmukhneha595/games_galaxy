from userInterface import *


def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("850x600")
    img = PhotoImage(file="snake_and_Ladder/lenna.gif")
    x = Display(master, img)
    master.mainloop()


main()
