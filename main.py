import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import cryptocode

window = Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)


def save_encrypt():
    title = title_entry.get()
    our_file = open("secret.txt", "a")
    note = secret_text.get("1.0", END)
    if len(secret_text.get("1.0", END)) == 1:
        tkinter.messagebox.showwarning("Text", "Enter Your Text")
    elif len(master_key_entry.get()) == 0:
        tkinter.messagebox.showwarning("Password","Pleas Enter Password")
    else:
        encoded = cryptocode.encrypt(message=note, password=master_key_entry.get())
        our_file.write(f"{title}\n{encoded}\n")
        our_file.close()
        title_entry.delete(0, END)
        secret_text.delete("1.0", END)
        master_key_entry.delete(0, END)


def decrypt_function():
    decoded = cryptocode.decrypt(secret_text.get("1.0", END), password=master_key_entry.get())
    if len(secret_text.get("1.0", END)) == 1 or master_key_entry.get() == "":
        tkinter.messagebox.showwarning("Warning", "Pleas Enter All Information")
    elif not decoded:
        tkinter.messagebox.showerror("Something Wrong", "Check Password Or Encrypted Info")
    else:
        secret_text.delete("1.0", END)
        secret_text.insert(INSERT, decoded)


# Image Part
img = ImageTk.PhotoImage(Image.open("secret-100.png"))
panel = Label(window, image=img, )
panel.pack()

# Text Parts
title_label = Label(text="Enter Your Title", font=("Arial", 13))
title_label.pack()

title_entry = Entry(width=45)
title_entry.pack()

secret_label = Label(text="Enter Your Secret", font=("Arial", 13))
secret_label.pack()

secret_text = Text(width=44, height=24)
secret_text.pack()

master_key_label = Label(text="Enter Master Key", font=("Arial", 13))
master_key_label.pack()

master_key_entry = Entry(width=45)
master_key_entry.pack()

save_button = Button(text="Save & Encrypt", command=save_encrypt)
save_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt_function)
decrypt_button.pack()

window.mainloop()
