import socket
from threading import Thread
from tkinter import *


nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")


class GUI:
    def __init__(self):
        self.window =Tk()
        self.window.withdraw()
        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False ,height=False)
        self.login.configure(width=400 ,height=300)

        self.pls = Label(self.login,text = "Please login to continue", justify = CENTER,font = "Helvetica 14 bold")
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)

        self.labelName = Label(self.login,text = "Name : ", font = "Helvetica 12")
        self.labelName.place(relheight = 0.2, relx = 0.1, rely = 0.2)

        self.entryName = Entry(self.login,font="Helvetica 14")
        self.entryName.place(relheight = 0.12, relwidth = 0.4, relx = 0.35, rely = 0.2)
        self.entryName.focus()

        self.goButton = Button(self.login,font="Helvetica 14 bold", text = "Continue", command = lambda:self.goAhead(self.entryName.get()))
        self.goButton.place(relx = 0.4, rely = 0.55)

        self.window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
        self.name = name
        rcv = Thread(target = self.receive)
        rcv.start() 
    
    def layout(self, name):
        self.name = name
        self.window.deiconify()
        self.window.title('CHAT ROOM')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg='#17202A')
        self.labelHead = Label(self.window, text=self.name, font='helvetica 13 bold', bg='#17202A', fg='#EAECEE', pady=5)
        self.labelHead.place(relwidth=1)

        self.line = Label(self.window, width=450, bg='#ABB2B9')
        self.line.place(relwidth=1, relheight=0.012, rely=0.07)

        self.textcons = Text(self.window, width=20, height=2, bg='#17202A', fg='#EAECEE', font='helvetica 14', padx=5, pady=5)
        self.textcons.place(relheight=0.745, relwidth=1, rely=0.08)

        self.labelBottom = Label(self.window, bg='#ABB2B9', height=80)
        self.labelBottom.place(relwidth=1, rely=0.025, )

        self.entryMessage = Entry(self.labelBottom, bg='#2C3E50', fg='#EAECEE', font='helvetica 13')
        self.entryMessage.place(relwidth=0.74, relheight=0.06,rely=0.008, relx=0.011)
        self.entryMessage.focus()

        self.buttonMessage = Button(self.labelBottom, text='Send', font='helvetica 10 bold', width=20, bg='#ABB2B9', command=lambda:self.sendButton)
        self.buttonMessage.place(relwidth=0.22, relheight=0.06, relx=0.77, rely=0.008)

        self.textcons.config(cursor='arrow')
        scrollBar = Scrollbar(self.textcons)
        scrollBar.place(relheight=1, relx=0.974)
        scrollBar.config(command=self.textcons.yview)
        self.textcons.config(state=DISABLED)
    
    def sendButton(self, message):
        self.textcons.config(state=DISABLED)
        self.message = message
        self.entryMessage.delete(0,END)
        snd = Thread(target=self.write)
        snd

    def receive():
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(nickname.encode('utf-8'))
                else:
                    print(message)
                    pass
            except:
                print("An error occured!")
                client.close()
                break

g = GUI()
"""
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()"""
