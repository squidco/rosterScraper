# Modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

# Components
from components.MenuBar import MenuBar

# Frames
from frames.SearchFrame import SearchFrame
from frames.TemplateFrame import TemplateFrame
from frames.FileCreationFrame import FileCreationFrame

# Classes
from classes.ColumnData import ColumnData
from classes.enums import Frames

# Services
from services.templateService import TemplateService

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Website Scraper")
        self.geometry("1000x400")
        self.option_add("*tearOff", False)

        # Style
        self.style = ttk.Style()

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
            sidebar, text="Search", command=lambda: self.changeFrame(Frames.SEARCH)
        )
        self.button.pack()

        self.button2 = ctk.CTkButton(
            sidebar, text="Sheet", command=lambda: self.changeFrame(Frames.SHEET)
        )
        self.button2.pack()

        self.button3 = ctk.CTkButton(
            sidebar, text="Templates", command=lambda: self.changeFrame(Frames.TEMPLATES)
        )
        self.button3.pack()

        # Frame container
        container = ctk.CTkFrame(self)
        container.pack(side="left", fill="both", expand=True)

        # Testing labels
        # label = ctk.CTkLabel(container, text="I am the container")
        # label2 = ctk.CTkLabel(container, text="I am the container")
        # label.pack(side="top")
        # label2.pack(side="bottom")

        # Frames
        self.frames = {}
        self.frames[Frames.SEARCH] = SearchFrame(
            container, self.url, self.tableIndex, self.changeFrame, self.importTable
        )
        self.frames[Frames.SHEET] = FileCreationFrame(
            container
        )
        self.frames[Frames.TEMPLATES] = TemplateFrame(container)

        self.changeFrame(Frames.SEARCH)

    # Helper Functions
    # Changes the visible frame in the container frame
    def changeFrame(self, index):
        for f in self.frames.values():
            f.forget()
        frame = self.frames[index]
        frame.pack(
            table=self.table, expand=True, fill="both"
        )  # Specific usage for the needs of the FileCreationFrame (Should change later)

    def importTable(self, table):
        self.table = table
        self.changeFrame(Frames.SHEET)  # Change to the File Creation Frame



if __name__ == "__main__":
    window = App()
    window.mainloop()
    sys.exit(0)

# TODO create the function that takes a template and retrieves the data
# TODO add option to name the output file
# TODO create a copy function to make copies of template files
# TODO detect if name/hometown columns are selected
# ONGOING work with pack more to get a decent layout
# ONGOING try to rename variables and arguments to be clear
# ONGOING give arguments datatypes (arg: type)
# ONGOING add comments to functions that need them
# TODO add menu options
## - file: show excel files
## - help: show an explanation of how to use the app
## - scrape: website (rename other option)
##           template (scrapes using preset options)
# TODO make the app record to the history of searches when searching for a website
# TODO auto-generate headshot paths
# (C:\ProgramData\AJT Systems\MAM\ESPN\LeagueAssets\NCAA\Headshots\lastname_firstname.png)

# DONE allow editing of column names
# DONE shows users what columns are selected
# DONE use explicit imports instead of star imports
# DONE refactor any repeated code into its own function
# DONE link up variables so everything works again
# DONE make the app record the last template used when creating an export file
