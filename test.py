import tkinter as tk

root = tk.Tk()
root.title("Scrollable Canvas Example")

# Create a Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="lightgray")
canvas.pack(side="left", fill="both", expand=True)

# Create a vertical Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Link the Scrollbar to the Canvas
canvas.config(yscrollcommand=scrollbar.set)

# Create a Frame to hold content and add it to the Canvas
content_frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Add widgets to the content_frame
for i in range(20):
    tk.Label(content_frame, text=f"Item {i+1}", padx=10, pady=5).pack()

# Update scrollregion when content_frame size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", on_frame_configure)

root.mainloop()