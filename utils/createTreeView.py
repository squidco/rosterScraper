import tkinter.ttk as ttk
import customtkinter as ctk


def createTreeView(parent, data, headingCallback=print):
    # TODO give none as the default arg for the callbacks and make sure that if they are left as none then the callbacks aren't added
    # Creates a treeview element from a 2d Array (or list or whatever)
    # The heading callback will have access to the index and value of the headings in a tuple
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both")

    table = ttk.Treeview(
        frame, style="Selection.Treeview", columns=data[0], show=("headings")
    )
    table.pack(fill="x")

    hsb = ttk.Scrollbar(frame, orient="horizontal", command=table.xview)
    table.configure(xscrollcommand=hsb.set)
    hsb.pack(side="bottom", fill="x")

    for i, value in enumerate(data[0]):  # Headings
        # This command= blob is broken down like so => lambda delays execution till click + j is a variable that captures the current val of i as the loop runs + the bit after : is just a callback
        table.heading(
            value,
            text=value,
            command=lambda dataTuple=(i, value): headingCallback(dataTuple),
        )
        table.column(value, minwidth=5)
        print(i, value)

    for r, row in enumerate(data[1:]):  # Rows
        table.insert(parent="", index=r, values=row)
