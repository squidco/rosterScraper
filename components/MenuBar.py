import tkinter as tk
from components.TemplateMenu import TemplateMenu

class MenuBar(tk.Menu):
    def __init__(self, parent, ts):
        super().__init__(parent)
        self.parent = parent
        self.ts = ts

        # Sub menus
        self.file = tk.Menu(self)
        self.add_cascade(menu=self.file, label="File")
        self.file.add_command(label="Exit", command=parent.quit)
        
        self.scrape = tk.Menu(self)
        self.add_cascade(menu=self.scrape, label="Scrape")
        
        self.template = TemplateMenu(self)
        # self.add_cascade(menu=self.template, label="Templates")
        
        
        self.help = tk.Menu(self)
        self.add_cascade(menu=self.help, label="Help")
    
    def openTemplateWindow(self):
        pass
        
    def fileMenu(self):
        pass

    def scrapeMenu(self):
        pass

    def helpMenu(self):
        pass