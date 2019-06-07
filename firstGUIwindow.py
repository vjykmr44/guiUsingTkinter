import tkinter

window = tkinter.Tk()

# to rename title of the window

window.title("GUI")

# pack is used to show the object in the window

label = tkinter.Label(window, text = "Hello world").pack()

window.mainloop()


