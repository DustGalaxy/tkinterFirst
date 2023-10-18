from tkinter.ttk import Notebook
from model.model import EEdSubject, EUserType, add_student, add_user, del_student, del_user, get_students_data, get_users_data, login_verify, set_teacher
from tkinter import Frame, Tk, Toplevel, Listbox, Label, Entry, Button, N, Variable, messagebox
from tkinter.font import Font
# from .create_parent_panel import CreateParentPanel
# from .create_teacher_panel import CreateTeacherPanel
# from .create_student_panel import CreateStudentPanel


class CreateParentPanel():
    
    def __init__(self, parent):
        
        self.root = Toplevel()
        self.parent: AdminPanel = parent
        #setting title
        self.root.title("Додати родителя")
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.desmiss()) 
        self.root.grab_set()
        #setting window size
        width=444
        height=270
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.fullname=Entry(self.root)
        self.fullname["borderwidth"] = "1px"
        ft = Font(family='Times',size=10)
        self.fullname["font"] = ft
        self.fullname["fg"] = "#333333"
        self.fullname["justify"] = "center"
        self.fullname["text"] = "Повне ім'я"
        self.fullname.place(x=70,y=40,width=300,height=30)

        self.GButton_469=Button(self.root)
        self.GButton_469["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=10)
        self.GButton_469["font"] = ft
        self.GButton_469["fg"] = "#000000"
        self.GButton_469["justify"] = "center"
        self.GButton_469["text"] = "Додати"
        self.GButton_469.place(x=70,y=190,width=155,height=30)
        self.GButton_469["command"] = self.create_parent_command

        self.GLabel_179=Label(self.root)
        ft = Font(family='Times',size=10)
        self.GLabel_179["font"] = ft
        self.GLabel_179["fg"] = "#333333"
        self.GLabel_179["justify"] = "center"
        self.GLabel_179["text"] = ""
        self.GLabel_179.place(x=70,y=230,width=303,height=30)

        self.login=Entry(self.root)
        self.login["borderwidth"] = "1px"
        ft = Font(family='Times',size=10)
        self.login["font"] = ft
        self.login["fg"] = "#333333"
        self.login["justify"] = "center"
        self.login["text"] = "Логин"
        self.login.place(x=70,y=90,width=300,height=30)

        self.password=Entry(self.root)
        self.password["borderwidth"] = "1px"
        ft = Font(family='Times',size=10)
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["justify"] = "center"
        self.password["text"] = "Пароль"
        self.password.place(x=70,y=140,width=300,height=30)

        self.GButton_402=Button(self.root)
        self.GButton_402["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=10)
        self.GButton_402["font"] = ft
        self.GButton_402["fg"] = "#000000"
        self.GButton_402["justify"] = "center"
        self.GButton_402["text"] = "Повернутися"
        self.GButton_402.place(x=260,y=190,width=110,height=30)
        self.GButton_402["command"] = self.desmiss

    def create_parent_command(self):
        if login_verify(self.login.get()):
            add_user(self.fullname.get(), self.login.get(), self.password.get(), EUserType.Parent.value)
            self.desmiss()
        else:
            self.GLabel_179["text"] = "Родич з таким логіном вже існує!"
        

    def desmiss(self):
        self.root.grab_release()
        self.parent.update_prnt()
        self.root.destroy()


class CreateStudentPanel():
    root: Toplevel
    student_fullname: Entry
    parents_list: Listbox
    create_student: Button
    status_label: Label
    
    std: str
    
    def __init__(self, parent):
        self.root = Toplevel()
        self.parent = parent
        #setting title
        self.root.title("Створити студента")
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.desmiss()) 
        self.root.grab_set()
        #setting window size
        width=290
        height=360
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.student_fullname = Entry(self.root)
        self.student_fullname["borderwidth"] = "1px"
        ft = Font(family='Times',size=10)
        self.student_fullname["font"] = ft
        self.student_fullname["fg"] = "#333333"
        self.student_fullname["justify"] = "center"
        self.student_fullname["text"] = "Entry"
        self.student_fullname.place(x=20,y=10,width=250,height=30)

        self.parents_list=Listbox(self.root, listvariable=Variable(value=[x[0] for x in get_users_data(EUserType.Parent)]))
        self.parents_list["borderwidth"] = "1px"
        ft = Font(family='Times',size=10)
        self.parents_list["font"] = ft
        self.parents_list["fg"] = "#333333"
        self.parents_list["justify"] = "center"
        self.parents_list.place(x=20,y=50,width=250,height=215)

        self.create_student=Button(self.root)
        self.create_student["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=10)
        self.create_student["font"] = ft
        self.create_student["fg"] = "#000000"
        self.create_student["justify"] = "center"
        self.create_student["text"] = "Button"
        self.create_student.place(x=80,y=280,width=125,height=30)
        self.create_student["command"] = self.create_student_command

        self.status_label=Label(self.root)
        ft = Font(family='Times',size=10)
        self.status_label["font"] = ft
        self.status_label["fg"] = "#333333"
        self.status_label["justify"] = "center"
        self.status_label["text"] = "label"
        self.status_label.place(x=20,y=320,width=250,height=30)
        
        
    def create_student_command(self):
        add_student(self.student_fullname.get(), get_users_data(EUserType.Parent)[self.parents_list.curselection()[0]][1])
        self.std = self.student_fullname.get()
        self.desmiss()
        
    def desmiss(self):
        self.root.grab_release()
        self.parent.update_std()
        self.root.destroy()


class CreateTeacherPanel():
    
    tch: str
    
    def __init__(self, parent):
        self.root = Toplevel()
        self.parent = parent
        #setting title
        self.root.title("Додати викладача")
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.desmiss()) 
        self.root.grab_set()
        #setting window size
        width=600
        height=270
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.fullname= Entry(self.root)
        self.fullname["borderwidth"] = "1px"
        ft = Font(family='Times',size=10)
        self.fullname["font"] = ft
        self.fullname["fg"] = "#333333"
        self.fullname["justify"] = "center"
        self.fullname["text"] = "Повне ім'я"
        self.fullname.place(x=70,y=40,width=300,height=30)

        GButton_469= Button(self.root)
        GButton_469["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=10)
        GButton_469["font"] = ft
        GButton_469["fg"] = "#000000"
        GButton_469["justify"] = "center"
        GButton_469["text"] = "Додати"
        GButton_469.place(x=70,y=190,width=155,height=30)
        GButton_469["command"] = self.create_teacher

        self.GLabel_179= Label(self.root)
        ft =  Font(family='Times',size=10)
        self.GLabel_179["font"] = ft
        self.GLabel_179["fg"] = "#333333"
        self.GLabel_179["justify"] = "center"
        self.GLabel_179["text"] = ""
        self.GLabel_179.place(x=70,y=230,width=303,height=30)

        self.login= Entry(self.root)
        self.login["borderwidth"] = "1px"
        ft =  Font(family='Times',size=10)
        self.login["font"] = ft
        self.login["fg"] = "#333333"
        self.login["justify"] = "center"
        self.login["text"] = "Логин"
        self.login.place(x=70,y=90,width=300,height=30)

        self.password= Entry(self.root)
        self.password["borderwidth"] = "1px"
        ft =  Font(family='Times',size=10)
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["justify"] = "center"
        self.password["text"] = "Пароль"
        self.password.place(x=70,y=140,width=300,height=30)

        self.GButton_402= Button(self.root)
        self.GButton_402["bg"] = "#f0f0f0"
        ft =  Font(family='Times',size=10)
        self.GButton_402["font"] = ft
        self.GButton_402["fg"] = "#000000"
        self.GButton_402["justify"] = "center"
        self.GButton_402["text"] = "Повернутися"
        self.GButton_402.place(x=260,y=190,width=110,height=30)
        self.GButton_402["command"] = self.GButton_402_command

        self.subject_list= Listbox(self.root, listvariable=Variable(value=[subj.name for subj in EEdSubject]))
        self.subject_list["borderwidth"] = "1px"
        ft =  Font(family='Times',size=10)
        self.subject_list["font"] = ft
        self.subject_list["fg"] = "#333333"
        self.subject_list["justify"] = "center"
        self.subject_list.place(x=390,y=40,width=140,height=180)

        
    def create_teacher(self):
        if login_verify(self.login.get()):
            user_id = add_user(self.fullname.get(), self.login.get(), self.password.get(), EUserType.Teacher.value)
            
            set_teacher(user_id, EEdSubject[f"{self.subject_list.get(self.subject_list.curselection()[0])}"].value)
            
            self.tch = self.fullname.get()
            self.desmiss()
        else:
            self.GLabel_179["text"] = "Користувач з таким логіном вже існує!"


    def GButton_402_command(self):
        self.desmiss()
        
        
    def tch_fullname(self):
        return self.tch
    
    def desmiss(self):
        self.root.grab_release()
        self.parent.update_tch()
        self.root.destroy()


class AdminPanel(Frame):
    
    def __init__(self, parent, notebook: Notebook, id: int):
        Frame.__init__(self, notebook)
        self.notebook = notebook
        self.parent = parent
        self.list_of_std = Variable(value=[f"{x[0]}, id: {x[1]}" for x in get_students_data()])
        self.list_of_prnt = Variable(value=[f"{x[0]}, login: {x[1]}, id: {x[2]}"  for x in get_users_data(EUserType.Parent)])
        self.list_of_tch = Variable(value=[f"{x[0]}, login: {x[1]}, id: {x[2]}"  for x in get_users_data(EUserType.Teacher)])
        
        # self.bind("<Activate>", self.update_all())
        
        self.parent_list=Listbox(self, listvariable=self.list_of_prnt)
        self.parent_list["borderwidth"] = "1px"
        ft = Font(family='Times',size=12)
        self.parent_list["font"] = ft
        self.parent_list["fg"] = "#333333"
        self.parent_list["justify"] = "center"
        self.parent_list.place(x=10,y=10,width=270,height=550)

        self.teacher_list=Listbox(self, listvariable=self.list_of_tch)
        self.teacher_list["borderwidth"] = "1px"
        ft = Font(family='Times',size=12)
        self.teacher_list["font"] = ft
        self.teacher_list["fg"] = "#333333"
        self.teacher_list["justify"] = "center"
        self.teacher_list.place(x=360,y=10,width=270,height=550)

        self.student_list=Listbox(self, listvariable=self.list_of_std)
        self.student_list["borderwidth"] = "1px"
        ft = Font(family='Times',size=12)
        self.student_list["font"] = ft
        self.student_list["fg"] = "#333333"
        self.student_list["justify"] = "center"
        self.student_list.place(x=710,y=10,width=270,height=550)
        
        create_parent=Button(self)
        create_parent["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        create_parent["font"] = ft
        create_parent["fg"] = "#000000"
        create_parent["justify"] = "center"
        create_parent["text"] = "Створити родителя"
        create_parent.place(x=10,y=570,width=230,height=30)
        create_parent["command"] = self.create_parent_command

        delete_parent=Button(self)
        delete_parent["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        delete_parent["font"] = ft
        delete_parent["fg"] = "#000000"
        delete_parent["justify"] = "center"
        delete_parent["text"] = "В"
        delete_parent.place(x=250,y=570,width=30,height=30)
        delete_parent["command"] = self.delete_parent_command

        create_teacher=Button(self)
        create_teacher["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        create_teacher["font"] = ft
        create_teacher["fg"] = "#000000"
        create_teacher["justify"] = "center"
        create_teacher["text"] = "Створити вчителя"
        create_teacher.place(x=360,y=570,width=230,height=30)
        create_teacher["command"] = self.create_teacher_command

        delete_teacher=Button(self)
        delete_teacher["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        delete_teacher["font"] = ft
        delete_teacher["fg"] = "#000000"
        delete_teacher["justify"] = "center"
        delete_teacher["text"] = "В"
        delete_teacher.place(x=600,y=570,width=30,height=30)
        delete_teacher["command"] = self.delete_teacher_command

        create_student=Button(self)
        create_student["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        create_student["font"] = ft
        create_student["fg"] = "#000000"
        create_student["justify"] = "center"
        create_student["text"] = "Створити студента"
        create_student.place(x=710,y=570,width=230,height=30)
        create_student["command"] = self.create_student_command

        delete_student=Button(self)
        delete_student["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        delete_student["font"] = ft
        delete_student["fg"] = "#000000"
        delete_student["justify"] = "center"
        delete_student["text"] = "В"
        delete_student.place(x=950,y=570,width=30,height=30)
        delete_student["command"] = self.delete_student_command
        
        exit=Button(self)
        exit["bg"] = "#f0f0f0"
        ft = Font(family='Times',size=12)
        exit["font"] = ft
        exit["fg"] = "#000000"
        exit["justify"] = "center"
        exit["text"] = "Вийти"
        exit.place(x=1000,y=10,width=50,height=30)
        exit["command"] = self.exit_tab
   
    def create_parent_command(self):
        CreateParentPanel(self) 
        
    def create_teacher_command(self):
        CreateTeacherPanel(self) 
        
    def create_student_command(self):
        CreateStudentPanel(self)
    
    def update_std(self):
        self.list_of_std.set([f"{x[0]}, id: {x[1]}" for x in get_students_data()])    

    def update_prnt(self):
        self.list_of_prnt.set([f"{x[0]}, login: {x[1]}, id: {x[2]}"  for x in get_users_data(EUserType.Parent)])

    def update_tch(self):
        self.list_of_tch.set([f"{x[0]}, login: {x[1]}, id: {x[2]}"  for x in get_users_data(EUserType.Teacher)])       

    # def update_all(self):
    #     self.list_of_std.set([f"{x[0]}, id: {x[1]}" for x in get_students_data()])
    #     self.list_of_prnt.set([f"{x[0]}, login: {x[1]}, id: {x[2]}"  for x in get_users_data(EUserType.Parent)])
    #     self.list_of_tch.set([f"{x[0]}, login: {x[1]}, id: {x[2]}" for x in get_users_data(EUserType.Teacher)]) 
    
    def delete_parent_command(self):
        if messagebox.askyesno("Підтвердження видалення", "Ви дісно бажаете видалити родителя?"):
            del_user(self.parent_list.selection_get().split()[-1])
            self.update_prnt()

    def delete_teacher_command(self):
        if messagebox.askyesno("Підтвердження видалення", "Ви дісно бажаете видалити вчителя?"):
            del_user(self.teacher_list.selection_get().split()[-1])
            self.update_tch()

    def delete_student_command(self):
        if messagebox.askyesno("Підтвердження видалення", "Ви дісно бажаете видалити учня?"):
            del_student(self.teacher_list.selection_get().split()[-1])
            self.update_std()
            
    def exit_tab(self):
        self.notebook.hide(self)
        self.notebook.add(self.parent)