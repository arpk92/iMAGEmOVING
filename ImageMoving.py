from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Image Mover")
# root.geometry("500x300+100+100")
first_image = ImageTk.PhotoImage(Image.open("/home/ar/PycharmProjects/Calculator/Image/g.jpeg")) #ChangeYourImagePath
second_image = ImageTk.PhotoImage(Image.open("/home/ar/PycharmProjects/Calculator/Image/b.jpeg"))
Third_image = ImageTk.PhotoImage(Image.open("/home/ar/PycharmProjects/Calculator/Image/c.jpeg"))
fourth_Image = ImageTk.PhotoImage(Image.open("/home/ar/PycharmProjects/Calculator/Image/d.jpeg"))
Five_Image = ImageTk.PhotoImage(Image.open("/home/ar/PycharmProjects/Calculator/Image/f.jpeg"))

image_list = [first_image, second_image, Third_image, fourth_Image, Five_Image]

lable = Label(image=first_image)
lable.grid(row=0, column=0, columnspan=3)
status = Label(root, text="Image 1 of " + str(len(image_list)))

#backwordFunction
def back(number):
    global lable
    global b1
    global b3
    lable.grid_forget()
    lable = Label(image=image_list[number - 1])
    b3 = Button(root, text=">>", command=lambda: faw(number + 1))
    b1 = Button(root, text="<<", command=lambda: back(number - 1))
    lable.grid(row=0, column=0, columnspan=3)
    b1.grid(row=1, column=0)
    b3.grid(row=1, column=2)
    status = Label(root, text="Image" + str(number) + "of " + str(len(image_list)))
    status.grid(row=2,column=0,columnspan=3)

#FawordFunction
def faw(number):
    global lable
    global b1
    global b2
    lable.grid_forget()
    lable = Label(image=image_list[number - 1])
    b3 = Button(root, text=">>", command=lambda: faw(number + 1))
    b1 = Button(root, text="<<", command=lambda: back(number - 1))
    lable.grid(row=0, column=0, columnspan=3)
    b1.grid(row=1, column=0)
    b3.grid(row=1, column=2)
    if number == 5:
        b3 = Button(root, text=">>", state=DISABLED)
    status = Label(root, text="Image" + str(number) + "of " + str(len(image_list)))
    status.grid(row=2,column=0,columnspan=3)


b1 = Button(root, text="<<", command=back)
b2 = Button(root, text="Exit Program", command=root.quit)
b3 = Button(root, text=">>", command=lambda: faw(2))
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
status.grid(row=2,column=0,columnspan=3)

root.mainloop()
#tutshouse.com
#thecomputercity.com
