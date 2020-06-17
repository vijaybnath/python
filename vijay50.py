import tkinter as tk

HEIGHT = 500
WIDTH = 600

def login(entry):
    print("This", entry, "was the recent login")

def cancel(entry2):
    print("this", entry2, "Was canceled")

def create(entry2):
    print("this", entry2, "Was created")

root = tk.Tk()
root.title("App")

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(canvas, bg='#80c1ff', bd=5)
frame.place(relx=0.6, rely=0.18, relwidth=0.75, relheight =0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Sign in", font=40, command=lambda :login(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
frame1.place(relx=0.6, rely=0.28, relwidth=0.75, relheight=0.1, anchor='n')

entry2 = tk.Entry(frame1, font=40)
entry2.place(relwidth=0.65, relheight=1)

button = tk.Button(frame1, text="Cancel", font=40, command=lambda :cancel(entry.get()))
button.place(relx=0.7, relheight=1.0, relwidth=0.3)

label = tk.Label(root, text="or create an account on this app", font=40)
label.place(relx=0.32, rely=0.4, relheight=0.05, relwidth=0.4)

label = tk.Label(root, text="Welcome to the app", font=40)
label.place(relx=0.28, rely=0.05, relheight=0.06, relwidth=0.5)

label1 = tk.Label(root, text="Sign in", font=30)
label1.place(relx=0.4, rely=0.10, relheight=0.05, relwidth=0.22)

label2 = tk.Label(root, text="Name", font=40)
label2.place(relx=0.08, rely=0.20, relheight=0.05, relwidth=0.14)

label = tk.Label(root, text="User Id", font=40)
label.place(relx=0.08, rely=0.30, relheight=0.05, relwidth=0.14)

frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
frame2.place(relx=0.22, rely=0.6, relheight=0.1, relwidth=0.75)

entry2 = tk.Entry(frame2, font=40)
entry2.place(relwidth=0.65, relheight=1)

button = tk.Button(frame2, text="Cancel",font=40, command=lambda :cancel(entry2.get()))
button.place(relx=0.7, relheight=1.0, relwidth=0.3)

label = tk.Label(root, text="First name", font=40)
label.place(relx=0.02, rely=0.45, relheight=0.10, relwidth=0.2)

label = tk.Label(root, text="Last Name", font=40)
label.place(relx=0.02, rely=0.6, relheight=0.10, relwidth=0.2)

frame3 = tk.Frame(root, bg='#80c1ff', bd=5)
frame3.place(relx=0.22, rely=0.45, relheight=0.1, relwidth=0.75)

entry2 = tk.Entry(frame3, font=40)
entry2.place(relwidth=0.65, relheight=1)

button = tk.Button(frame3, text="Create",font=40, command=lambda :create(entry2.get()))
button.place(relx=0.7, relheight=1.0, relwidth=0.3)

root.mainloop()