import tkinter
from pynput.keyboard import Controller, Key


class Button(object):
    def __init__(
            self,
            name,
            location_x,
            location_y,
            key,
            picture,
            width,
            height):
        self.name = name
        self.loc_x = location_x
        self.loc_y = location_y
        self.key = key
        self.picture = picture
        self.width = width
        self.height = height

    def pushbutton(self):
        kb = Controller()

        kb.press(Key.ctrl)
        kb.press(Key.alt)
        kb.press(self.key)

        kb.release(Key.ctrl)
        kb.release(Key.alt)
        kb.release(self.key)

        global image1, button1, ssbutton
        ssbutton.state = 1
        image1 = tkinter.PhotoImage(file="./button/stop.gif")
        button1 = tkinter.Button(win32, image=image1,
                                 command=ssbutton.pushbutton,
                                 width=ssbutton.width,
                                 height=ssbutton.height)
        button1.place(x=ssbutton.loc_x, y=ssbutton.loc_y, anchor="nw")
        win32.update_idletasks()


class SSButton(Button):
    def __init__(
            self,
            name,
            location_x,
            location_y,
            key,
            picture,
            width,
            height,
            state):
        Button.__init__(
            self,
            name,
            location_x,
            location_y,
            key,
            picture,
            width,
            height)
        self.state = state

    def pushbutton(self):
        kb = Controller()

        kb.press(Key.ctrl)
        kb.press(Key.alt)
        kb.press(self.key)

        kb.release(Key.ctrl)
        kb.release(Key.alt)
        kb.release(self.key)

        if self.state == 0:
            self.state = 1
            self.picture = "./button/stop.gif"
        else:
            self.state = 0
            self.picture = "./button/start.gif"
        global image1, button1
        image1 = tkinter.PhotoImage(file=self.picture)
        button1 = tkinter.Button(win32, image=image1,
                                 command=ssbutton.pushbutton,
                                 width=ssbutton.width,
                                 height=ssbutton.height)
        button1.place(x=ssbutton.loc_x, y=ssbutton.loc_y, anchor="nw")
        win32.update_idletasks()


ssbutton = SSButton("start", 480, 200, "p", "./button/start.gif", 232, 367, 0)
next_button = Button("next", 812, 200, Key.right, "./button/next.gif", 330, 367)
last_button = Button("last", 50, 200, Key.left, "./button/last.gif", 330, 367)


# 初始化窗口
win32 = tkinter.Tk()

# 设置标题
win32.title("音乐控制器")

label = tkinter.Label(win32,
                      text="网易云音乐\n控制器",
                      bg="white", fg="red",
                      font=("微软雅黑", 40),
                      width=2000,
                      height=1000,
                      justify="right",
                      anchor="ne")
label.pack()


# 创建按钮
image1 = tkinter.PhotoImage(file=ssbutton.picture)
button1 = tkinter.Button(win32, image=image1,
                         command=ssbutton.pushbutton,
                         width=ssbutton.width,
                         height=ssbutton.height)
button1.place(x=ssbutton.loc_x, y=ssbutton.loc_y, anchor="nw")

image3 = tkinter.PhotoImage(file=next_button.picture)
button3 = tkinter.Button(win32, image=image3,
                         command=next_button.pushbutton,
                         width=next_button.width,
                         height=next_button.height)
button3.place(x=next_button.loc_x, y=next_button.loc_y, anchor="nw")


image4 = tkinter.PhotoImage(file=last_button.picture)
button4 = tkinter.Button(win32, image=image4,
                         command=last_button.pushbutton,
                         width=last_button.width,
                         height=last_button.height)
button4.place(x=last_button.loc_x, y=last_button.loc_y, anchor="nw")


win32.geometry("1250x667+200+50")

win32.mainloop()
