
from tkinter import Tk, Toplevel, Listbox, Label, Entry, Button, N, Frame, Variable, StringVar
from tkinter.ttk import Notebook
from tkinter.font import Font
from model.model import get_students_data, get_academic_performance, get_users_data, EUserType, EEdSubject



class ParentPanel(Frame):
    def __init__(self, parent, notebook: Notebook, id: int):
        Frame.__init__(self, notebook)
        self.notebook = notebook
        self.parent = parent
        self.id = id
        self.ed_eff = Variable(value=[  f"{get_students_data(int(var['student_id']))[0]},  " + 
                                        f"Предмет: {EEdSubject(var['subject_id']).name},  " +
                                        f"Оцінка: {var['grade']},  " +
                                        f"Відвідуваність: {var['attendance_rate']}" for var in get_academic_performance(self.id)])
        var = str(get_users_data(EUserType.Parent, self.id)[0])
        self.parent_name = StringVar(value=var)
        
        ft = Font(family='Times',size=12)
        
        GListBox_381=Listbox(self, listvariable=self.ed_eff)
        GListBox_381["borderwidth"] = "1px"
        GListBox_381["font"] = ft
        GListBox_381["fg"] = "#333333"
        GListBox_381["justify"] = "center"
        GListBox_381.place(x=10,y=50,width=452,height=471)

        GButton_182=Button(self)
        GButton_182["bg"] = "#f0f0f0"
        GButton_182["font"] = ft
        GButton_182["fg"] = "#000000"
        GButton_182["justify"] = "center"
        GButton_182["text"] = "Оновити"
        GButton_182.place(x=480,y=70,width=100,height=30)
        GButton_182["command"] = self.GButton_182_command

        GLabel_671=Label(self, textvariable=self.parent_name)
        GLabel_671["anchor"] = "nw"
        GLabel_671["font"] = ft
        GLabel_671["fg"] = "#333333"
        GLabel_671["justify"] = "center"
        GLabel_671["text"] = "label"
        GLabel_671.place(x=10,y=10,width=240,height=30)

        GButton_162=Button(self)
        GButton_162["bg"] = "#f0f0f0"
        GButton_162["font"] = ft
        GButton_162["fg"] = "#000000"
        GButton_162["justify"] = "center"
        GButton_162["text"] = "Вийти"
        GButton_162.place(x=480,y=10,width=100,height=30)
        GButton_162["command"] = self.GButton_162_command

    def GButton_182_command(self):
        self.ed_eff.set([f"{get_students_data(int(var['student_id']))[0]},  " + 
                         f"Предмет: {EEdSubject(var['subject_id']).name},  " +
                         f"Оцінка: {var['grade']},  " +
                         f"Відвідуваність: {var['attendance_rate']}" for var in get_academic_performance(self.id)])


    def GButton_162_command(self):
        self.notebook.hide(self)
        self.notebook.add(self.parent)