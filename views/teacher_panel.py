from tkinter.ttk import Notebook
from model.model import EEdSubject, EUserType, add_academic_performance, get_academic_performance_tch, get_students_data, get_tch_subject, get_users_data, set_academic_performance
from tkinter import Frame, StringVar, Tk, Toplevel, Listbox, Label, Entry, Button, N, Variable
from tkinter.font import Font

class CreateAcPfPanel():
    def __init__(self, parent, subject: EEdSubject) -> None:
        self.root = Toplevel()
        self.parent = parent
        self.subject: EEdSubject = subject
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.desmiss()) 
        self.root.grab_set()
        
        self.root.title("Додати успішність учня")
        width=608
        height=400
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.std_list = Variable(value=[f"{std[0]}, {std[1]}" for std in get_students_data()])
        self.text_grade = StringVar()
        self.text_rate = StringVar()
        self.status: StringVar = StringVar()

        ft = Font(family='Times',size=12)

        grade = Entry(self.root, 
                      borderwidth="1px", 
                      font=ft, 
                      justify="center", 
                      textvariable=self.text_grade,)
        

        rate = Entry(self.root, 
                     borderwidth= "1px",
                     font=ft,
                     justify="center",
                     textvariable=self.text_rate)
        
        
        confirm = Button(
                        self.root, 
                        font=ft, 
                        justify="center", 
                        text="Підтвердити",
                        width="17",
                        command=self.confirm_command)          
        
        cancel = Button(
                        self.root, 
                        font=ft, 
                        justify="center", 
                        text="Відмінити", 
                        width="17",
                        command=self.cancel_command)
        

        self.list_std_2 = Listbox(self.root, listvariable=self.std_list)
        self.list_std_2["borderwidth"] = "1px"
        self.list_std_2["font"] = ft
        self.list_std_2["fg"] = "#333333"
        self.list_std_2["justify"] = "center"
        

        GLabel_74_2 = Label(self.root)
        GLabel_74_2["font"] = ft
        GLabel_74_2["fg"] = "#333333"
        GLabel_74_2["justify"] = "center"
        GLabel_74_2["text"] = "Оцінка"
        
        
        GLabel_298_2 = Label(self.root)
        GLabel_298_2["font"] = ft
        GLabel_298_2["fg"] = "#333333"
        GLabel_298_2["justify"] = "center"
        GLabel_298_2["text"] = "Відвідуваність"
        
        
        status_label_2 = Label(self.root, textvariable=self.status, width="30")
        status_label_2["font"] = ft
        status_label_2["fg"] = "#333333"
        status_label_2["justify"] = "center"
        status_label_2["text"] = ""
        
        GLabel_74_2.    grid(row = 0, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        grade.          grid(row = 1, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        GLabel_298_2.   grid(row = 2, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        rate.           grid(row = 3, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        status_label_2. grid(row = 4, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        confirm.        grid(row = 5, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        cancel.         grid(row = 6, column = 1, ipadx=10, ipady=6, padx=5, pady=5)
        self.list_std_2.     grid(row = 0, column = 0, rowspan = 7, padx=5, pady=5)
        
    def confirm_command(self):
        try:
            id = self.list_std_2.get(first=self.list_std_2.curselection()[0]).split()[-1]
            subject = self.subject.value
            grade = float(self.text_grade.get())
            rate = float(self.text_rate.get())
            add_academic_performance(id, subject, grade, rate)
            self.status.set(value="Дані додані")
        except Exception:
            self.status.set(value="Некоректні данні")

    def cancel_command(self):
        self.desmiss()

    def desmiss(self):
        self.parent.update_list()
        self.root.grab_release()
        self.root.destroy()


class UpdateAcPfPanel():
    def __init__(self, parent, id) -> None:
        self.root = Toplevel()
        self.parent = parent
        self.id = id
        
        self.text_grade = StringVar()
        self.text_rate = StringVar()
        self.status = StringVar()
        
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.desmiss()) 
        
        
        self.root.title("Оновити успішність")
        
        
        
        width=223
        height=340
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        
        self.root.grab_set()
        
        ft = Font(family='Times',size=12)
        
        GLabel_74=Label(self.root, width=200, font=ft, justify="center", text="Оцінка")
        GLabel_74.pack(anchor=N,padx=8, pady=8)
        
        grade = Entry(self.root, width=200, font=ft, justify="center", textvariable = self.text_grade)
        grade.pack(anchor=N,padx=8, pady=8)
        
        GLabel_298=Label(self.root, width=200, font=ft, justify="center", text="Відвідуваність")
        GLabel_298.pack(anchor=N,padx=8, pady=8)
        
        rate = Entry(self.root, width=200, font=ft, justify="center", textvariable = self.text_rate)
        rate.pack(anchor=N,padx=8, pady=8)
        
        confirm=Button(self.root, 
                            width=200, 
                            font=ft,
                            justify="center",
                            text="Підтвердити",
                            command = self.confirm_command)
        
        confirm.pack(anchor=N,padx=8, pady=8)
        
        cancel=Button(self.root, 
                            width=200, 
                            font=ft,
                            justify="center",
                            text="Відмінити",
                            command = self.cancel_command)
        cancel.pack(anchor=N,padx=8, pady=8)
        
        status_label = Label(self.root, width=200, font=ft, justify="center", textvariable=self.status)
        status_label.pack(anchor=N,padx=8, pady=8)
        
        
    def confirm_command(self):
        try:
            set_academic_performance(self.id, float(self.text_grade.get()), float(self.text_rate.get()))
            self.status = StringVar(value="Оновленні додані")
        except Exception:
            self.status = StringVar(value="Некоректні данні")
            
    def cancel_command(self):
        self.desmiss()

    def desmiss(self):
        self.parent.update_list()
        self.root.grab_release()
        self.root.destroy()


class TeacherPanel(Frame):
    def __init__(self, parent, notebook: Notebook, id: int) -> None:
        Frame.__init__(self, notebook)
        
        self.notebook = notebook
        self.parent = parent
        self.id = id
        self.subject = get_tch_subject(self.id)
        self.student_list = Variable(value=[f"{std[0]},  Оцінка: {std[3]},  Відвідуваність: {std[4]}, id: {std[-1]}" for std in get_academic_performance_tch(self.subject)])
        
        
        ft = Font(family='Times',size=12)
        
        tch_name=Label(self)
        tch_name["font"] = ft
        tch_name["fg"] = "#333333"
        tch_name["justify"] = "center"
        tch_name["text"] = f"{get_users_data(EUserType.Teacher, id)[0]}"
        tch_name.place(x=10,y=10,width=179,height=30)

        exit=Button(self)
        exit["bg"] = "#f0f0f0"
        exit["font"] = ft
        exit["fg"] = "#000000"
        exit["justify"] = "center"
        exit["text"] = "Вихід"
        exit.place(x=500,y=10,width=89,height=30)
        exit["command"] = self.desmiss

        self.std_list = Listbox(self, listvariable=self.student_list)
        self.std_list["borderwidth"] = "1px"
        self.std_list["font"] = ft
        self.std_list["fg"] = "#333333"
        self.std_list["justify"] = "center"
        self.std_list.place(x=20,y=50,width=568,height=392)

        create_ac_pf = Button(self)
        create_ac_pf["bg"] = "#f0f0f0"
        create_ac_pf["font"] = ft
        create_ac_pf["fg"] = "#000000"
        create_ac_pf["justify"] = "center"
        create_ac_pf["text"] = "Створити запис"
        create_ac_pf.place(x=20,y=450,width=200,height=30)
        create_ac_pf["command"] = self.create_ac_pf_command

        set_ac_pf = Button(self)
        set_ac_pf["bg"] = "#f0f0f0"
        set_ac_pf["font"] = ft
        set_ac_pf["fg"] = "#000000"
        set_ac_pf["justify"] = "center"
        set_ac_pf["text"] = "Змінити запис"
        set_ac_pf.place(x=390,y=450,width=200,height=30)
        set_ac_pf["command"] = self.set_ac_pf_command

    def desmiss(self):
        self.notebook.hide(self)
        self.notebook.add(self.parent)

    def create_ac_pf_command(self):
        ert = CreateAcPfPanel(self, self.subject)

    def set_ac_pf_command(self):
        ieo = UpdateAcPfPanel(self, self.std_list.get(first=self.std_list.curselection()[0]).split()[-1])
        
    def update_list(self):
        self.student_list.set(value=[f"{std[0]},  Оцінка: {std[3]},  Відвідуваність: {std[4]}, id: {std[-1]}" for std in get_academic_performance_tch(self.subject)])
