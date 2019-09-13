from tkinter import *
import tkinter.font as font
def printhello():
    print("Hello")

root = Tk() # create window
root.title("Hello World!")
# create label
lbl1 = Label(root, text='Hello tkinter...')
lbl1.pack()
hellobtn = Button(root, text="Greet",
                  width = 30,
                  command=printhello)
hellobtn['font'] = font.Font(size=20,
                             weight='bold')
hellobtn.pack()
quitbtn = Button(root, text="Quit",fg ="red",
                 bg = "white",
                 font=font.Font(size=20),
                 command=root.quit)
quitbtn.pack()
root.mainloop() # present window - blocking

# after closing window
print("Goodbye...")
