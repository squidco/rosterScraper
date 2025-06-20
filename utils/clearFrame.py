def clearFrame(frame):
    # Clear the window
    for widget in frame.winfo_children():
        widget.destroy()