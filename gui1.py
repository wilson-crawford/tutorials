import Tkinter as tkinter

window = tkinter.Tk()


window.title("Super-Cool Window")
# window.wm_iconbitmap("youriconhere.ico")

# This is what you want to add, it is a label
lbl = tkinter.Label(window, text="This is a nice label")
# =============================================

window.geometry("500x500")

window.mainloop()
