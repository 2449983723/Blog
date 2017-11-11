# coding=utf-8
from Tkinter import *
root = Tk()

android = ['liunian', 'chenkai']
ios = ['jinlin', 'longwei']

androidListbox = Listbox(root)
iosListbox = Listbox(root)

for item in android:
    androidListbox.insert(0, item)

for item in ios:
    iosListbox.insert(0, item)

androidListbox.pack()
iosListbox.pack()

root.mainloop()
