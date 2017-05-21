#import the 'tkinter' module
import Tkinter
#create a new window
window = Tkinter.Tk()
#set the window title
window.title("Super-Cool window")
#set the window size
window.geometry("300x300")
#set the window icon
window.wm_iconbitmap('favicon.ico')
#draw the window, and start the 'application'
window.mainloop()
