
from tkinter.font import Font
from tkinter.ttk import Frame, Notebook
from tkinter import END, Label, Entry, Button, N
from model.model import login
from views.admin_panel import AdminPanel
from views.parent_panel import ParentPanel
from views.teacher_panel import TeacherPanel


class LoginPanel(Frame):
    error_label: Label
    login_enrty: Entry
    password_entry: Entry
    mode: str
   
    def __init__(self, parent):
        self.notebook: Notebook = parent
        Frame.__init__(self, parent)
        self.focus()
        
        self.login_enrty = Entry(self)
        self.login_enrty.pack(anchor=N, padx=8, pady=8)
        self.password_entry = Entry(self)
        self.password_entry.pack(anchor=N, padx=8, pady=8)
        
        
        self.error_label = Label(self)
        self.error_label.pack(anchor=N, padx=8, pady=8)
        
        self.login_button = Button(self, text="Вхід", command=lambda: self.try_login(self.login_enrty.get(), self.password_entry.get()))
        ft = Font(family='Times',size=12)
        self.login_button["font"] = ft
        self.login_button.place(width=70, height=40)
        self.login_button.pack(anchor="center", expand=1) 
        self.login_enrty.focus()
        self.pack()

    def try_login(self, login_name: str, password: str):
        user = login(login_name, password)
        if user:
            mode = user['user_type']
            match mode:        
                case "0":
                    return
                case "1":
                    self.notebook.add(AdminPanel(self, self.notebook, int(user['user_id'])), text="Адмін")                 
                    self.notebook.hide(self)
                case "2":
                    self.notebook.add(TeacherPanel(self, self.notebook, int(user['user_id'])), text="Вчитель")
                    self.notebook.hide(self)
                case "3":
                    self.notebook.add(ParentPanel(self, self.notebook, int(user['user_id'])), text="Родитель")
                    self.notebook.hide(self)
            self.login_enrty.delete(0, last=END)
            self.password_entry.delete(0, last=END)
        else:
            self.error_label["text"] = "No users?"        