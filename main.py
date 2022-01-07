"""Верный PIN: 1234, первоначальная сумма на карте: 10000, при переведе необходимо ввести номер карты из 16 цифр"""


from tkinter import *
from PIL import ImageTk, Image
import sys


class Bank(Frame):
    p = ''
    can_pass = ''
    money = 10000

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        super().__init__()
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.load_image()
        self.center_window()
        self.start_screen()
        self.panel()
        self.place_card()
        self.card()
        self.flag = 0
        self.flag2 = False

    def start_screen(self):
        """Начальный черный экран"""
        black_screen = Canvas(self)
        black_screen.create_rectangle(200, 50, 600, 350, outline="black", fill="black", width=2)
        black_screen.pack(fill=BOTH, expand=1)

    def center_window(self):
        """Создание окна по центру экрана"""
        w = 800
        h = 600

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def load_image(self):
        """Загрузка изображений"""
        try:
            self.img0 = Image.open("images/0.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img1 = Image.open("images/1.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img2 = Image.open("images/2.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img3 = Image.open("images/3.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img4 = Image.open("images/4.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img5 = Image.open("images/5.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img6 = Image.open("images/6.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img7 = Image.open("images/7.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img8 = Image.open("images/8.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img9 = Image.open("images/9.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img = Image.open("images/empty.jpg").resize((50, 50), Image.ANTIALIAS)
            self.img_cancel = Image.open("images/cancel.jpg").resize((100, 50), Image.ANTIALIAS)
            self.img_clear = Image.open("images/clear.jpg").resize((100, 50), Image.ANTIALIAS)
            self.img_enter = Image.open("images/enter.jpg").resize((100, 50), Image.ANTIALIAS)
            self.img_empty = Image.open("images/emptylong.jpg").resize((100, 50), Image.ANTIALIAS)
            self.img_card = Image.open("images/card.jpg").resize((150, 75), Image.ANTIALIAS)
            self.back = Image.open("images/back.jpg").resize((400, 300), Image.ANTIALIAS)
        except IOError:
            print("Возникла ошибка во время открытия изображения!")
            sys.exit(1)

    def place_card(self):
        """Место куда прикладывать карту."""
        self.pack(fill=BOTH, expand=1)
        can_place = Canvas(self)
        label = Label(can_place, text='Приложите карту', font='Roboto 12', fg='black', bg='#808080')
        can_place.create_rectangle(0, 0, 200, 150, fill="#808080")
        label.place(x=35, y=10)
        can_place.place(x=575, y=400)

    def card(self):
        """Ваша карта."""
        self.img_card = ImageTk.PhotoImage(self.img_card)
        canvas = Canvas(self, width=150, height=73, highlightthickness=0)
        canvas.create_image(75, 35, anchor=CENTER, image=self.img_card)
        canvas.place(x=20, y=450)

        def drag(event):
            """Метод, двигающий карту"""
            mouse_x = self.winfo_pointerx() - self.winfo_rootx()
            mouse_y = self.winfo_pointery() - self.winfo_rooty()
            event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)
            if (578 < event.widget.winfo_x() < 624) and (440 < event.widget.winfo_y() < 470) and (self.flag == 0) \
                    and (self.flag2 == False):
                self.flag = 1
                self.flag2 = True
                self.password()

        canvas.bind("<B1-Motion>", drag)  # левая кнопка мыши нажата

    def password(self):
        """Окно для ввода пароля."""
        __class__.can_pass = Canvas(self, width=150, height=73, highlightthickness=0)
        main_label = Label(__class__.can_pass, text='Введите PIN', font='Arial 15', justify=CENTER, padx=10, pady=10)
        main_label.pack()
        textExample = Entry(__class__.can_pass, bg='#fff', fg='#444', font='Arial 12')
        textExample.pack()
        __class__.can_pass.place(x=320, y=100)
        __class__.p = textExample

    def panel(self):
        """Создание кнопок на нижней панели"""
        def click_button(text):
            """Команды кнопок"""
            if text == "clear":
                Bank.p.delete(len(Bank.p.get()) - 1)

            elif text == "enter":
                if self.flag == 1:
                    if Bank.p.get().isdigit():
                        if Bank.p.get() == '1234':
                            Bank.can_pass.place_forget()
                            Bank.next_screen(self)
                            self.flag = 1
                elif self.flag == 2:
                    if Bank.p.get().isdigit():
                        if int(Bank.p.get()) < int(Bank.money):
                            Bank.money -= int(Bank.p.get())
                            Bank.can_pass.place_forget()
                            self.flag = 1
                elif self.flag == 3:
                    if Bank.p.get().isdigit():
                        Bank.money += int(Bank.p.get())
                        Bank.can_pass.place_forget()
                        self.flag = 1
                elif self.flag == 4:
                    if len(Bank.p.get()) == 16 and Bank.p.get().isdigit():
                        Bank.can_pass.place_forget()
                        Bank.next_stage(self)

            elif text == "cancel":
                if self.flag == 1:
                    Bank.can_pass.place_forget()
                    self.flag = 0
                elif self.flag == 0:
                    Bank.quit(self)
                elif self.flag == 2 or self.flag == 3 or self.flag == 4:
                    Bank.can_pass.place_forget()
                    self.flag = 0

            else:
                Bank.p.insert(INSERT, text)

        can_panel = Canvas(width=200, height=150)
        can_panel.place(x=250, y=375)

        img0 = ImageTk.PhotoImage(self.img0)
        but0 = Button(can_panel, image=img0, command=lambda: click_button("0"))

        img1 = ImageTk.PhotoImage(self.img1)
        but1 = Button(can_panel, image=img1, command=lambda: click_button("1"))

        img2 = ImageTk.PhotoImage(self.img2)
        but2 = Button(can_panel, image=img2, command=lambda: click_button("2"))

        img3 = ImageTk.PhotoImage(self.img3)
        but3 = Button(can_panel, image=img3, command=lambda: click_button("3"))

        img4 = ImageTk.PhotoImage(self.img4)
        but4 = Button(can_panel, image=img4, command=lambda: click_button("4"))

        img5 = ImageTk.PhotoImage(self.img5)
        but5 = Button(can_panel, image=img5, command=lambda: click_button("5"))

        img6 = ImageTk.PhotoImage(self.img6)
        but6 = Button(can_panel, image=img6, command=lambda: click_button("6"))

        img7 = ImageTk.PhotoImage(self.img7)
        but7 = Button(can_panel, image=img7, command=lambda: click_button("7"))

        img8 = ImageTk.PhotoImage(self.img8)
        but8 = Button(can_panel, image=img8, command=lambda: click_button("8"))

        img9 = ImageTk.PhotoImage(self.img9)
        but9 = Button(can_panel, image=img9, command=lambda: click_button("9"))

        img = ImageTk.PhotoImage(self.img)
        but = Button(can_panel, image=img)
        but_1 = Button(can_panel, image=img)

        img_cancel = ImageTk.PhotoImage(self.img_cancel)
        but_cancel = Button(can_panel, image=img_cancel, command=lambda: click_button("cancel"))
        img_clear = ImageTk.PhotoImage(self.img_clear)
        but_clear = Button(can_panel, image=img_clear, command=lambda: click_button("clear"))
        img_enter = ImageTk.PhotoImage(self.img_enter)
        but_enter = Button(can_panel, image=img_enter, command=lambda: click_button("enter"))
        img_empty = ImageTk.PhotoImage(self.img_empty)
        but_empty = Button(can_panel, image=img_empty)

        but0.image = img0
        but1.image = img1
        but2.image = img2
        but3.image = img3
        but4.image = img4
        but5.image = img5
        but6.image = img6
        but7.image = img7
        but8.image = img8
        but9.image = img9
        but.image = img
        but_1.image = img
        but_cancel.image = img_cancel
        but_clear.image = img_clear
        but_enter.image = img_enter
        but_empty.image = img_empty

        but0.grid(row=4, column=2)
        but1.grid(row=1, column=1)
        but2.grid(row=1, column=2)
        but3.grid(row=1, column=3)
        but4.grid(row=2, column=1)
        but5.grid(row=2, column=2)
        but6.grid(row=2, column=3)
        but7.grid(row=3, column=1)
        but8.grid(row=3, column=2)
        but9.grid(row=3, column=3)
        but.grid(row=4, column=1)
        but_1.grid(row=4, column=3)
        but_cancel.grid(row=1, column=4)
        but_clear.grid(row=2, column=4)
        but_enter.grid(row=3, column=4)
        but_empty.grid(row=4, column=4)


    def next_screen(self):
        """Экран после ввода PIN, с действующими кнопками"""
        def click(text):
            """Действие после нажатия кнопки"""
            if text == 'баланс' and (self.flag != 2) and (self.flag != 3) and (self.flag != 4):
                Bank.can_pass = Canvas(self, width=50, height=50, highlightthickness=0)
                main_label = Label(Bank.can_pass, text='Ваш баланс {0}'.format(Bank.money), font='Arial 15', justify=CENTER, padx=10,
                                   pady=10)
                main_label.pack()
                Bank.can_pass.place(x=300, y=100)
                self.flag = 2
            if text == 'снять' and (self.flag != 2) and (self.flag != 3) and (self.flag != 4):
                Bank.can_pass = Canvas(self, width=50, height=50, highlightthickness=0)
                main_label = Label(Bank.can_pass, text='Введите сумму для снятия. \nБаланс: {0}'.format(Bank.money), font='Arial 15',
                                   justify=CENTER, padx=20,
                                   pady=10)
                textExample = Entry(Bank.can_pass, bg='#fff', fg='#444', font='Arial 12')
                main_label.pack()
                textExample.pack()
                Bank.p = textExample
                Bank.can_pass.place(x=240, y=70)
                self.flag = 2
            if text == 'пополнить' and (self.flag != 2) and (self.flag != 3) and (self.flag != 4):
                Bank.can_pass = Canvas(self, width=50, height=50, highlightthickness=0)
                main_label = Label(Bank.can_pass, text='Введите сумму для пополения', font='Arial 15',
                                   justify=CENTER, padx=10,
                                   pady=10)
                textExample = Entry(Bank.can_pass, bg='#fff', fg='#444', font='Arial 12')
                main_label.pack()
                textExample.pack()
                Bank.p = textExample
                Bank.can_pass.place(x=240, y=100)
                self.flag = 3
            if text == 'перевести' and (self.flag != 2) and (self.flag != 3) and (self.flag != 4):
                Bank.can_pass = Canvas(self, width=50, height=50, highlightthickness=0)
                main_label = Label(Bank.can_pass, text='Введите номер карты получателя:', font='Arial 15',
                                   justify=CENTER, padx=10,
                                   pady=10)
                textExample = Entry(Bank.can_pass, bg='#fff', fg='#444', font='Arial 12')
                main_label.pack()
                textExample.pack()
                Bank.p = textExample
                Bank.can_pass.place(x=240, y=100)
                self.flag = 4

        self.back = ImageTk.PhotoImage(self.back) #создание фона
        screen = Canvas(self)
        label = Label(screen, image=self.back)
        label.pack()

        """Созданик кнопок"""
        withdraw = Button(screen, text='Снять', font='Roboto 14', justify=CENTER, padx=35, pady=10, fg='black',
                          bg='white', relief=RIDGE, borderwidth=0, command=lambda: click("снять"))
        withdraw.place(x=250, y=150)
        top_up = Button(screen, text='Пополнить', font='Roboto 14', justify=CENTER, padx=11, pady=10, fg='black',
                       bg='white', relief=RIDGE, borderwidth=0, command=lambda: click("пополнить"))
        top_up.place(x=250, y=220)
        balance = Button(screen, text='Баланс', font='Roboto 14', justify=CENTER, padx=27, pady=10, fg='black',
                        bg='white', relief=RIDGE, borderwidth=0, command=lambda: click("баланс"))
        balance.place(x=30, y=150)
        transfer = Button(screen, text='Перевести', font='Roboto 14', justify=CENTER, padx=11, pady=10, fg='black',
                         bg='white', relief=RIDGE, borderwidth=0, command=lambda: click("перевести"))
        transfer.place(x=30, y=220)
        screen.place(x=198, y=48)

    def next_stage(self):
        """Вторая стадия перевода денег, срабатывает если выполнена первая стадия."""
        Bank.can_pass = Canvas(self, width=50, height=50, highlightthickness=0)
        main_label = Label(Bank.can_pass, text='Введите сумму для перевода', font='Arial 15',
                           justify=CENTER, padx=10,
                           pady=10)
        textExample = Entry(Bank.can_pass, bg='#fff', fg='#444', font='Arial 12')
        main_label.pack()
        textExample.pack()
        Bank.p = textExample
        Bank.can_pass.place(x=240, y=100)
        self.flag = 2

def main():
    root = Tk()
    Bank(root)
    root.mainloop()


if __name__ == '__main__':
    main()
