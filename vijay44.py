import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def Cancel():
    return False

def Done():
    return True

button = tk.Button(font="15", text="Done", command=Done())
button.pack()

button1 = tk.Button(font="15", text="Cancel", command=Cancel())
button1.pack()

root.mainloop()