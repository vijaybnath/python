import tkinter as  tk

HEIGHT = 700
WIDTH = 600
root = tk.Tk()
root.title("App")

tk.Label(root, text="First Name").grid(row=0)
tk.Label(root, text="Last Name").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


root.mainloop()