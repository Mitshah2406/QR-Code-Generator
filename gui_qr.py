from tkinter import *
import pyqrcode   #module for creating qr code
from PIL import Image,ImageTk #module for opening qr code
import png #module for setting size of qr code

root = Tk()

def generate():
    name = name_entry.get()
    url = url_entry.get()
    file = name + ".png"
    qrcode= pyqrcode.create(url)
    qrcode.png(file,scale =7)
    image = ImageTk.PhotoImage(Image.open(file))
    image_label = Label(image= image)
    image_label.image = image
    canvas.create_window(295,200,window = image_label)


root.title("QR Code Generator")

canvas = Canvas(root,height=400,width=600)
canvas.pack()

app_label = Label(root,text="QR Code Generator",fg='blue',font=('Arial',20))
canvas.create_window(300,50,window= app_label)

name_label = Label(root,text="Enter The Name Of The Link: ")
canvas.create_window(300,100,window=name_label)
url_label = Label(root,text="Enter The URL: ")
canvas.create_window(300,160,window=url_label)


name_entry = Entry(root)
url_entry = Entry(root)
canvas.create_window(300,130,window=name_entry)
canvas.create_window(300,180,window=url_entry)

gen_btn = Button(root,text="Generate QR Code",command=lambda:generate())
canvas.create_window(300,220,window=gen_btn)
root.mainloop()