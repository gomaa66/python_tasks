import math
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image

def ButtonPressTracker():
    ButtonPressTracker.counter +=1 
    print("The button pressed" , ButtonPressTracker.counter)
ButtonPressTracker.counter =0

def large():
    price =15
    large.count+=1
    result=price*large.count 
    print("the price is : ",result)
large.count=0
def meduim():
    price =10
    meduim.count+=1
    result=price*meduim.count 
    print("the price is : ",result)
meduim.count=0
def small():
    price = 5
    small.count+=1
    result=price*small.count 
    print("the price is : ",result)
small.count=0
    
 




window_1=Tk()
window_1.title(" 2sab Shop")
window_1.geometry('600x600')
#To Exit the window 
b1=Button(window_1,text="Exit Window",bd='5',command=window_1.destroy)
b1.pack(side=BOTTOM)

Label_1=Label(window_1 ,text ="WELCOME TO 2asab shop :)")
#used to set the lable in specicied place
Label_1.pack(side=TOP)
#used to set main window size 
#To choose the size of the drinken 2sab

#TO PUT an image on the Button
Small_size=PhotoImage(file='Small.png')
Small_size=Small_size.subsample(2,2)
Small=Button(window_1,text="Small Size",bd='5',image=Small_size,background="green",fg="blue",command=small)
Small.place(x=400,y=50)

Mid_size=PhotoImage(file='Mid.png')
Mid_size=Mid_size.subsample(2,2)
Mid=Button(window_1,text="Mid Size",bd='5',image=Mid_size,background="green",fg="blue",command=meduim)
Mid.place(x=230,y=50)

Large_size=PhotoImage(file='Large.png')
Large_size=Large_size.subsample(2,2)
Large=Button(window_1,text="Large Size",bd='5',image=Large_size,background="green",fg="blue",command=large)
Large.place(x=50,y=50)



window_1.mainloop()