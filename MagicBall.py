from tkinter import * #imports the entire tkinter library
from tkinter import messagebox #Imports the text boxes
import random #imports the things to get pick the ansewer
#thanks asehlaoui for the base code

root = Tk() #blank window called 'root'
root.title("Magicball")#names the window
root.geometry("650x650+0+0") #size of root window

heading = Label( root, text="Lets find the awnser!", font=("arial", 15, "bold"), fg="red").pack() #creates a heading of text
label_question = Label(root, text="Please enter your question:", font=("arial", 20, "bold"), fg="green").place(x=10, y=500) #Places on the screen(root)

photo1 = PhotoImage(file='ball.png') #loads the picture
picture = Label(root, image=photo1, bg="black") .place(x=200, y=50) #places the picture

nameEntry_box = Entry(root, width=25, bg="white") #creates the name entry box
nameEntry_box.place(x=390, y=512) #defines the place of the entry box

def check_name(): #creates the function to be called once the button is pressed
     
    question = nameEntry_box.get()

    the = random.randint(1, 50) #generates a random number 1 through 50

    if question == "": 
        messagebox.showinfo("Error","Enter Question")

    #Sees if you typed a message if not will display Enter Question with the window title Error
    if question =="Does Stephen have a girlfriend?":
        messagebox.showinfo("Answer","NO")

    if question == "Does Vincent have a girlfriend?":
        messagebox.showinfo("Answer","YES")

    if question =="Does Emilia have a boyfriend":
        messagebox.showinfo("Answer","Yes, 5")

    if question == "Does Vincent like Lucy?":
        messagebox.showinfo("Answer","No, he loves Eve")

    if question == "Does Emilia have a crush?":
        messagebox.showinfo("Answer","Yes, She has 5")

    if question == "Is the Magicball incorrect?":
        messagebox.showinfo("Answer","NO")

    if question == "Is Stephen smart and handsome?":
        messagebox.showinfo("Answer","YES")

    elif the == 1:
        messagebox.showinfo("Answer","It is certain")
    #sees if "the" a vairble that has a numeber 1 through 50, then displayes the special message
    elif the == 2:
        messagebox.showinfo("Answer","Outlook good")

    elif the == 3:
        messagebox.showinfo("Answer","You may rely on it")

    elif the == 4:
        messagebox.showinfo("Answer","Ask again later")

    elif the == 5:
        messagebox.showinfo("Answer","Concentrate and ask again")

    elif the == 6:
        messagebox.showinfo("Answer","Reply hazy, try again")

    elif the == 7:
        messagebox.showinfo("Answer","My reply is no")

    elif the == 8:
        messagebox.showinfo("Answer","My sources say no")

    elif the == 9:
        messagebox.showinfo("Answer","Why do you need to know.")

    elif the == 10:
        messagebox.showinfo("Answer","Stephen is all knowing so go ask him")

    elif the == 11:
        messagebox.showinfo("Answer","Just forget about it.")

    elif the == 12:
        messagebox.showinfo("Answer","Ask your mom see knows all.")

    elif the == 13:
        messagebox.showinfo("Answer","You always knew it.")

    elif the == 14:
        messagebox.showinfo("Answer","ALL MY SOURCES SAY NO.")

    elif the == 14:
        messagebox.showinfo("Answer","Better not tell you now.")

    elif the == 15:
        messagebox.showinfo("Answer","Outlook not so good.")

    elif the == 16:
        messagebox.showinfo("Answer","Count on it.")

    elif the == 17:
        messagebox.showinfo("Answer","Just Forget about it.")

    elif the == 18:
        messagebox.showinfo("Answer","IDK. Try again.")

    elif the == 19:
        messagebox.showinfo("Answer","Ask google.")

    elif the == 20:
        messagebox.showinfo("Answer","I am not your assistent.")

    elif the == 21:
        messagebox.showinfo("Answer","Ask your neighbor, not me.")

    elif the == 22:
        messagebox.showinfo("Answer","Noway!")

    elif the == 23:
        messagebox.showinfo("Answer","Do a backflip and ask again.")

    elif the == 24:
        messagebox.showinfo("Answer","Put food in power port and ask again.")

    elif the == 25:
        messagebox.showinfo("Answer","Somewhat.")

    elif the == 26:
        messagebox.showinfo("Answer","My all mighty anwser is no.")

    elif the == 27:
        messagebox.showinfo("Answer","Probaly No")

    elif the == 28:
        messagebox.showinfo("Answer","Probaly Yes")

    elif the == 29:
        messagebox.showinfo("Answer","YeSsSsSsSs")

    elif the == 30:
        messagebox.showinfo("Answer","Sure")

    elif the == 31:
        messagebox.showinfo("Answer","Stop spamming the machine.")

    elif the == 32:
        messagebox.showinfo("Answer","Hmmmmmmmmmmmmmmmm. NO")

    elif the == 33:
        messagebox.showinfo("Answer","Maybe Yes.")

    elif the == 34:
        messagebox.showinfo("Answer","Sadly No.")

    elif the == 35:
        messagebox.showinfo("Answer","Sadly Yes.")

    elif the == 36:
        messagebox.showinfo("Answer","This is a waste of your time.")

    elif the == 37:
        messagebox.showinfo("Answer","Thats a stupid question.")

    elif the == 38:
        messagebox.showinfo("Answer","404 Error")

    elif the == 39:
        messagebox.showinfo("Answer","What would Stephen do.")

    elif the == 40:
        messagebox.showinfo("Answer","Absoulutly.")

    elif the == 41:
        messagebox.showinfo("Answer","Outlook not so good")

    elif the == 42:
        messagebox.showinfo("Answer","YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs.")

    elif the == 43:
        messagebox.showinfo("Answer","NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.")

    elif the == 44:
        messagebox.showinfo("Answer","HMMMMMMMMMMMMMMMMMMMMMMMMMMMM Yes.")

    elif the == 45:
        messagebox.showinfo("Answer","Lost in translation")

    elif the == 46:
        messagebox.showinfo("Answer","Go ask another machine.")

    elif the == 47:
        messagebox.showinfo("Answer","You'll never know.")

    elif the == 48:
        messagebox.showinfo("Answer","I am sorry to say but yes.")

    elif the == 49:
        messagebox.showinfo("Answer","I am sorry to say but no.")

    elif the == 50:
        messagebox.showinfo("Answer","You are stupid to ask that question")

check = Button(root, text="Check Now", width=30, height=5, bg="white", command= check_name).place(x=200, y=550) #creates the button and calls the function to be executed

root.mainloop() #makes the window stay open forever
