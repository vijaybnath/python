import tkinter as tk

HEIGHT = 600
WIDTH = 600

def search(entry):
    print()

root = tk.Tk()
root.title("App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.04, relheight=0.07, relwidth=0.79, anchor='n')

entry=tk.Entry(frame, font=40)
entry.place(relheight=1, relwidth=0.69)

button = tk.Button(frame, text="Search", font=40, command= lambda: search(entry.get()))
button.place(relx=0.7, relheight=1.0, relwidth=0.3) 

frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
frame1.place(relx=0.5, rely=0.2, relheight=0.7, relwidth=0.79, anchor='n')

root.mainloop()