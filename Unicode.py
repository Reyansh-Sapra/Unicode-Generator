from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Random Unicode")

def unicode_it():
    codes = ["\u6342", "\u5235", "\u4647", "\u6353", "\u7875", "\u6454", "\u8758", "\u9755" "\u6443", "\u7457", "\u5767", "\u4758", "\u8476", "\u6445", "\u1234", "\u7534", "\u7543", "\u3764", "\u3444", "\u3745", "\u7445", "\u8475", "\u4787", "\u4654", "\u3543", "\u4657", '\u0394', "\ue000", "\u0e55", "\u0e57", "\u4500", "\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685", "\u2686", "\u6453", "\u8383", "\u1089", "\u2048", "\u2929", "\u8888", "\u1111", "\u2020", "\u1000", "\u8585", "\u9999" ]
    chosen = random.choice(codes)
    my_label.config(text=chosen)
                                                                                                                                                                                                                                                                                            

button = Button(root, text="Get Random Unicode text image", font=("Times New Roman", 22), fg="green", bg="black", command=unicode_it)                                         
button.pack(pady=20)

my_label = Label(root, text="", font=("Helvetica", 100))
my_label.pack(pady=17)

root.mainloop()