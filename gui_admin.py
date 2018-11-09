from tkinter import *
from tkinter import messagebox
import os
import sys

#setup general parameters for tkinter
window = Tk()
window.title("System Admin")
window.geometry('200x80')

 
def add_photo():
    import face_dataset
    face_dataset.main()
    #print("adding photo")

def train():
    import face_training
    face_training.main()
    #print("train")

def main():
    add_btn = Button(window,text='Register', command=add_photo)
    add_btn.grid(column=0,row=0)
    train_btn = Button(window,text='Train data', command=train)
    train_btn.grid(column=30,row=30)

     
    window.mainloop()

if __name__ == "__main__":
    main()
