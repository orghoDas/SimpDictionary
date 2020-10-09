from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches


data = json.load(open('data.json'))


# WINDOW
window = Tk()
window.title('SimpDictionary')


# BACKGROUND
image = Image.open('OED2_volumes.jpg')
photo_image = ImageTk.PhotoImage(image)


# WINDOW LABEL
label = Label(window, image= photo_image)
label.pack()


# ENTRY
e1_value = StringVar()
e1 = Entry(window, textvariable='Input', bg='#FFFD38', fg='black', justify=CENTER, font=('calibri', 30, 'bold'))
e1.place(relx=.185, rely=0.70, relwidth=.63, relheight=.082)


# SEARCH BUTTON
b1 = Button(window, text='Search', bg='green', fg='white', font=('calibri', 30, 'bold'), command = lambda : search(e1_value))
b1.place(relx=.40, rely=.85, relwidth=.2, relheight=.052)


# OUTPUT DEFINITION
t1 = Text(window, fg='#fff', relief=FLAT, bg='#444444', font=('calibri', 30, 'bold'))
t1.place(relx=0.185, rely=.05, relwidth=.63, relheight=.20)

window.mainloop()