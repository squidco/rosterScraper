from tkinter import *
from tkinter.ttk import *

class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)

        # Sub menus
        self.menuFile = Menu(self)
        self.menuScrape = Menu(self)
        self.menuHelp = Menu(self)
        self.add_cascade(menu=self.menuFile, label="File")
        self.add_cascade(menu=self.menuScrape, label="Scrape")
        self.add_cascade(menu=self.menuHelp, label="Help")

        self.menuFile.add_command(label="Exit", command=parent.quit)
        self.menuScrape.add_command(label="Search", command=parent.openScrapeWindow)

    def fileMenu(self):
        pass

    def scrapeMenu(self):
        pass

    def helpMenu(self):
        pass