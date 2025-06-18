from tkinter import *
from tkinter.ttk import *

import tableScraper


def clearFrame(frame):
    # Clear the window
    for widget in frame.winfo_children():
        widget.destroy()


class App(Tk):
    def __init__(self):
        super().__init__()
        self.data = None

        # Window config
        self.title("Roster Scraper")
        self.geometry("600x400")
        self.option_add("*tearOff", False)

        # widgets
        ## Menubar
        self.menubar = MenuBar(self)
        self["menu"] = self.menubar

        ## Table
        self.tableFrame = Frame(self)
        self.columnData = tableScraper.ColumnData()

        ## Create excel button
        self.createButton = Button(
            self, text="Create File", command=lambda: self.fileClick()
        )
        self.createButton.pack()

    def openScrapeWindow(self):
        # Clear the window and create a new search window
        self.searchWindow = SearchWindow(self)

    def headingClick(self, column):
        if column in self.columnData.columns:
            self.columnData.columns.remove(column)
        else:
            self.columnData.columns.append(column)
        print(self.columnData.columns)

    def fileClick(self):
        print(self.columnData.columns)
        df = tableScraper.createDfFromData(self.columnData, self.data)
        tableScraper.create_excel(df)

    def importTable(self, data):
        self.data = data

        clearFrame(self.tableFrame)

        table = Treeview(self.tableFrame, columns=self.data[0], show="headings")
        table.pack()

        for i, value in enumerate(self.data[0]):  # Headings
            # This command= blob is broken down like so => lambda delays execution till click + j is a variable that captures the current val of i as the loop runs + the bit after : is just a callback
            table.heading(value, text=value, command=lambda j=(i,value): self.headingClick(j))
            print(i, value)

        for r, row in enumerate(self.data[1:]):  # Rows
            table.insert(parent="", index=r, values=row)

        self.tableFrame.pack()


# TODO make the button that does stuff, do stuff
class SearchWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Scrape")
        self.geometry("800x800")
        self.tables = None
        self.selectedTable = IntVar()

        # Widgets and layout
        self.columnconfigure((0, 1, 2), weight=0)
        self.rowconfigure((0, 1, 2), weight=0)

        self.searchFrame = Search(self)
        self.separator = Separator(self, orient=VERTICAL)  # TODO fix this
        self.tableFrames = Frame(self)

        self.searchFrame.grid(column=0, row=0, sticky=(N, W))
        self.separator.grid(column=0, row=0)
        self.tableFrames.grid(column=2, row=0, sticky=(N, W))

    def createTableSelectionWindow(self, tables):
        self.tables = tables

        # Clear any existing frames in `self.tableFrames`
        clearFrame(self.tableFrames)

        # Create table frames
        for i, table in enumerate(tables):
            tableFrame = Frame(self.tableFrames, relief=RIDGE, padding=5)
            radio = Radiobutton(tableFrame, value=i, variable=self.selectedTable)
            radio.grid(column=0, row=0, sticky=(N))

            # Create rows and columns
            for r, row in enumerate(table):
                if r < 5:  # Only get the first 5 entries
                    for c, value in enumerate(row):
                        label = Label(tableFrame, text=value)
                        label.grid(column=c, row=r + 1, sticky=(E, W))
                else:
                    break

            tableFrame.grid(column=1, row=i, sticky=(N, W))

    def handleImportButton(self, table):
        self.parent.importTable(self.tables[table.get()])
        pass


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


class Search(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Vars
        self.url = StringVar()
        self.tables = None
        self.selectedTable = parent.selectedTable

        # Widgets and layout
        self.createWidgets()

    def createWidgets(self):
        # Create the widgets for the search frame
        ## URL group
        urlLabel = Label(self, text="Input the URL of the roster page:")
        urlEntry = Entry(self, textvariable=self.url)

        ## Search button
        searchButton = Button(
            self,
            text="Scrape",
            default=ACTIVE,
            command=lambda: self.scrapeButtonClick(self.url.get()),
        )

        importButton = Button(
            self,
            text="Import Table",
            default=ACTIVE,
            command=lambda: self.parent.handleImportButton(self.selectedTable),
        )

        # Configure the grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Place the widgets in the grid
        urlLabel.grid(column=0, row=0, sticky=(W, E))
        urlEntry.grid(column=1, row=0, sticky=(W, E))
        searchButton.grid(column=1, row=1, sticky=(W, E))
        importButton.grid(column=1, row=2, sticky=(W, E))

    def scrapeButtonClick(self, url):
        tables = tableScraper.url_get_content(url).tables
        self.parent.createTableSelectionWindow(tables)
