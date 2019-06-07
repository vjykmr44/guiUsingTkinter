import tkinter

window = tkinter.Tk()

# to rename title of the window

window.title("GUI")

# creating a frame

top_frame = tkinter.Frame(window).pack(side = "bottom")

btn3 = tkinter.Button(top_frame, text = "Button2", fg = "purple").pack(side = "left")

window.mainloop()


