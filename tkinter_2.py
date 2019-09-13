from tkinter import *

def printhello():
    print("Hello")

root = Tk() # create window
root.title("Hello World!")
# create label
lbl1 = Label(root, text='Hello tkinter...')
lbl1.pack()
hellobtn = Button(root, text="Greet",
                  command=printhello)
hellobtn.pack()
quitbtn = Button(root, text="Quit",
                 command=root.quit)
quitbtn.pack()
root.mainloop() # present window - blocking

# after closing window
print("Goodbye...")
