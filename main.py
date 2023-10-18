from tkinter.font import Font
from tkinter.ttk import Frame, Notebook
from tkinter import BOTH, END, Listbox, StringVar, Toplevel, Button, Tk, Variable, Label, Entry, N, messagebox
from views.login_panel import LoginPanel
# from model.model import *

"""
Контроль за школярами. 
Кожний школяр (як і всі  користувачі) ідентифікується системою і додається директором,  
результати його навчання (присутність, оцінки) визначаються  вчителями. 
Батьки можуть переглядати інформацію тільки про власних дітей. 
"""
    
class App:    
    def __init__(self):
        self.root = Tk()
        width = 1100
        height = 700
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=True, height=False)
        self.root.title("Програма для пергляду учнів")
        
        self.tabs_control = Notebook(self.root, height=700, width=800)
        
        self.login_tab = LoginPanel(self.tabs_control)
        
        self.tabs_control.add(self.login_tab, text="login")
        
    def d(self):
        self.root.destroy()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()
            
    def draw_widgets(self):
        self.tabs_control.pack(fill=BOTH)
        self.tabs_control.select
        

if __name__ == "__main__":
    app = App()
    app.run()

