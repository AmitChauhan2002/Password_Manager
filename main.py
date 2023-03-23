from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GeneratePassowrd():
    """Will automatically generate password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_length = 20
    Choice_1 = [letters,numbers,symbols]
    password = ""

    for i in range(0,nr_length):
        rand_1 = random.choice(Choice_1)

        if rand_1 == letters:
            letter = random.choice(letters)
            password += letter

        elif rand_1 == numbers:
            number = random.choice(numbers)
            password += number

        else:
            symbols = random.choice(symbols)
            password += symbols
        
    PasswordEntry.delete(0,END)
    PasswordEntry.insert(0,password)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.config(padx=50,pady=50)
windows.title("Password Manager")

canvas = Canvas(height=200,width=200)
logoImage = PhotoImage(file="C:/Users/Amit Chauhan/Desktop/100_Days_Python/Day_29/PasswordManager/logo.png")
logo = canvas.create_image(100,100,image = logoImage)
canvas.grid(row=0,column=1)

WebsiteLabel = Label(text="Website: ")
WebsiteLabel.grid(row=1,column=0)
WebsiteEntry = Entry(width=45)
WebsiteEntry.grid(row=1,column=1,columnspan=2)
# focus will automatically bring the curson to webseite entry at the starting of a programmer
WebsiteEntry.focus()

EmailLabel = Label(text="Email/Username: ")
EmailLabel.grid(row=2,column=0)
EmailEntry = Entry(width=45)
EmailEntry.grid(row=2,column=1,columnspan=2)
# insert method will automatically pre populate the entry space
# 0 means 0 index
EmailEntry.insert(0,"example@gmail.com")

PasswordLabel = Label(text="Password: ")
PasswordLabel.grid(row=3,column=0)
PasswordEntry = Entry(width=28)
PasswordEntry.grid(row=3,column=1)

GeneratePasswordButton = Button(text="Generate",width=8,command=GeneratePassowrd)
GeneratePasswordButton.grid(row=3,column=2)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# converting password to cipher than saving it 


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+','@','.']

direction = "encode" 
shift = 5
def encrypt_decrypt(text):
    """Will convert the password in cypher code"""
    newString = list(text)
    increment = 0
    while increment != len(newString):
        if newString[increment] != " ":
            index = alphabet.index(newString[increment])
            if direction[0] == "e":
                newIndex = index + shift
            else:
                newIndex = index - shift
            if newIndex <= (len(alphabet) - 1):
                newString[increment] = alphabet[newIndex]
            else:
                secondIndex = newIndex - (len(alphabet))
                newString[increment] = alphabet[secondIndex]
        increment+=1
    EncodedPassowrd = listToString(newString)
    return EncodedPassowrd

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def save():
    """Will save the credentials to a text file"""
    # messagebox.showinfo(title="Password Manager",message="Password Saved")
    # messagebox.askyesno("Password Manager","Save Password")
    windows.clipboard_clear()
    if WebsiteEntry.get() == "" or EmailEntry.get() == "" or PasswordEntry.get() == "":
        messagebox.showwarning(title="Warning",message="Please fill all the entries")
    else:
        is_ok = messagebox.askokcancel(title=WebsiteEntry.get(),message=f"These are the datails entered: \nEmail: {EmailEntry.get()} \nPassword: {PasswordEntry.get()} \nIs it ok to save")
        if is_ok:
            with open("C:/Users/Amit Chauhan/Desktop/100_Days_Python/Day_29/PasswordManager/password.txt",mode="a") as file:
                encodeData = messagebox.askyesno("Encode Data",message="Would you like to encode the data before saving")
                if encodeData == True:
                    file.write(f"\n{encrypt_decrypt(WebsiteEntry.get())} | {encrypt_decrypt(EmailEntry.get())} | {encrypt_decrypt(PasswordEntry.get())}")
                else:
                    file.write(f"\n{WebsiteEntry.get()} | {EmailEntry.get()} | {PasswordEntry.get()}")
                clipBoard = messagebox.askyesno("Copy to clipboard",message="Would you like to copy password to clipboard")
                if clipBoard == True:
                    windows.clipboard_clear()
                    windows.clipboard_append(PasswordEntry.get())
            WebsiteEntry.delete(0,END)
            EmailEntry.delete(0,END)
            PasswordEntry.delete(0,END)

AddButton = Button(width=35,text="Add",command=save)
AddButton.grid(row=4,column=1,columnspan=2)

windows.mainloop()