# Modules
import sys
import tkinter as tk
import customtkinter as ctk

# Components
from components.MenuBar import MenuBar
from components.SearchFrame import SearchFrame
from components.FileCreationFrame import FileCreationFrame

# Custom Module
import tableScraper

# Classes
from classes.Template import Template
from classes.ColumnData import ColumnData

# Services
from services.templateService import TemplateService


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Website Scraper")
        self.geometry("1000x400")
        self.option_add("*tearOff", False)

        # Services
        self.ts = TemplateService()

        # Variables
        self.table = None
        self.selectedFrame = tk.IntVar()  # Index of current frame displaying
        self.tableIndex = tk.IntVar()
        self.columnData = ColumnData()
        self.url = tk.StringVar()

        # Widgets
        ## Menubar
        self.menubar = MenuBar(self, self.ts)
        self.configure(menu=self.menubar)

        # Side bar
        sidebar = ctk.CTkFrame(self)
        sidebar.pack(side="left", fill="y")

        self.button = ctk.CTkButton(
            sidebar, text="Search", command=lambda: self.changeFrame(0)
        )
        self.button.pack()

        self.button2 = ctk.CTkButton(
            sidebar, text="Table", command=lambda: self.changeFrame(1)
        )
        self.button2.pack()

        # Frame container
        container = ctk.CTkFrame(self)
        container.pack(side="left", fill="both", expand=True)

        # Frames
        self.frames = {}
        self.frames[0] = SearchFrame(
            container, self.url, self.tableIndex, self.changeFrame, self.importTable
        )
        self.frames[1] = FileCreationFrame(
            container, self.table, self.createExcelSheet, self.headingClick
        )

        self.changeFrame(self.selectedFrame.get())

    # Helper Functions
    # Changes the visible frame in the container frame
    def changeFrame(self, index):
        for f in self.frames.values():
            f.forget()
        frame = self.frames[index]
        frame.pack(table=self.table, expand=True, fill="both")

    # Event handlers
    # TODO add on specific heading name checks
    def headingClick(self, column):
        if column in self.columnData.columns:
            self.columnData.columns.remove(column)
        else:
            self.columnData.columns.append(column)

    def createExcelSheet(self):
        # Create excel sheet
        df = tableScraper.createDfFromData(self.columnData, self.table)
        tableScraper.create_excel(df)

        # Create template to save last search
        template = Template(self.url.get(), self.tableIndex.get(), self.columnData)
        self.ts.updateLast(template)

    def importTable(self, table):
        self.table = table
        self.changeFrame(1)  # Change to the File Creation Frame


if __name__ == "__main__":
    window = App()
    window.mainloop()
    sys.exit(0)

# TODO create the function that takes a template and retrieves the data
# TODO create a copy function to make copies of template files?
# TODO work with pack more to get a decent layout - in progress -
# Done: refactor any repeated code into its own function
# TODO try to rename variables and arguments to be clear
# TODO give arguments datatypes (arg: type)
# TODO add option to name the output file
# TODO detect if name/hometown columns are selected
# TODO add comments to functions that need them
# TODO use explicit imports instead of star imports
# TODO add menu options
## - file: show excel files
## - help: show an explanation of how to use the app
## - scrape: website (rename other option)
##           template (scrapes using preset options)
# TODO allow renaming of columns
# TODO auto-generate headshot paths
# (C:\ProgramData\AJT Systems\MAM\ESPN\LeagueAssets\NCAA\Headshots\lastname_firstname.png)


# done link up variables so everything works again
# done make the app record the last template used when creating an export file
# TODO make the app record to the history of searches when searching for a website
