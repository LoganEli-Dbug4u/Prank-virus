root = tk.Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(width=FALSE, height=FALSE)
import tkinter as tk

def donothing():
    pass

main = tk.Tk()
main.protocol('WM_DELETE_WINDOW',donothing)
main.mainloop()
