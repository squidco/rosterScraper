import tkinter.ttk as ttk
import customtkinter as ctk

def createTreeView(parent, data, headingCallback=print, doubleClick=print):
    # TODO give none as the default arg for the callbacks and make sure that if they are left as none then the callbacks aren't added
    # Creates a treeview element from a 2d Array (or list or whatever)
    # The heading callback will have access to the index and value of the headings in a tuple
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both")

    tree = ttk.Treeview(
        frame, style="Selection.Treeview", columns=data[0], show=("headings")
    )
    tree.pack(fill="x")

    # Horizontal Scrollbar
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(side="bottom", fill="x")

    # Events
    tree.bind("<Double-1>", lambda: doubleClick(tree.selection()[0]))

    for i, value in enumerate(data[0]):  # Headings
        # This command= blob is broken down like so => lambda delays execution till click + j is a  variable that captures the current val of i as the loop runs + the bit after : is just a     callback
        tree.heading(
            value,
            text=value,
            command=lambda dataTuple=(i, value): headingCallback(dataTuple),
        )
        tree.column(value, minwidth=5)
        print(i, value)

    for r, row in enumerate(data[1:]):  # Rows
        tree.insert(parent="", index=r, values=row)
