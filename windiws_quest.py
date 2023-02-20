from tkinter import *


def showraven():
    room1 = Toplevel()
    room1.resizable(False, False)
    room1.geometry('1080x720+100+100')

    room1['bg'] = 'gray22'

    text1 = Label(
        room1,
        text='Выберете все правильные математические равенства.\n(Если равенство верно , то при нажатии кнопка пропадет)\n(Правельных равенств ровно 3) ',
        fg='white', background='gray22', font='Arial 30')
    text1.pack()

    # Buttons
    button1 = Button(room1, text='2+2=4', fg='blue')
    button1.place(x=200, y=100)

    button2 = Button(room1, text='6*6=36', fg='blue')
    button2.place(x=200, y=130)

    button3 = Button(room1, text='4^2=16', fg='blue')
    button3.place(x=200, y=160)
    # -----------------------------------------------------------------
    button4 = Button(room1, text='99+8=108', fg='blue')
    button4.place(x=200, y=190)

    button5 = Button(room1, text='3+3=7', fg='blue')
    button5.place(x=200, y=210)

    button6 = Button(room1, text='3+3>3*2', fg='blue')
    button6.place(x=200, y=240)

    room1.mainloop()


if __name__ == '__main__':
    showraven()
