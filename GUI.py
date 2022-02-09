from cgitb import text
import tkinter as tk
from tkinter import CENTER, Variable, ttk
from PIL import Image, ImageTk
import random
import lists as ls


freunde = ["weibl", "männl", "sächl"]
farben = ["blau", "grün", "weiß"]
musik = ["pop", "rock", "edm"]
liste_Auswahl = ["family", "numbers", "sports", "colors", "songs", "foods", "movies", "hobbies", "characteristics", "things", "languages"]
auswahl_Dict = {"family": ls.family, "numbers": ls.numbers, "sports": ls.sports, "colors": ls.colors, "songs": ls.songs, "foods": ls.foods, "movies": ls.movies, "hobbies": ls.hobbies, "characteristics":ls.characteristics, "things": ls.things, "languages": ls.lanuages}

def printEntryInput(selection):
    return(chosenList.get())
def howItWorks():
   hierKoennte.set(random.choice(auswahl_Dict[chosenList.get()]))

root = tk.Tk()
root.title("Random Generator")
root.geometry("800x400")
root.minsize(width=250, height=250)
root.maxsize(width=600, height=600)
root.resizable(width=False, height=True)
buttonText = tk.StringVar()
buttonText.set("Push it")
number = tk.IntVar()
number.set(10)
numberDecimal = tk.DoubleVar()
numberDecimal.set(5.8)
boolTime = tk.BooleanVar()
boolTime.set(True)
image = Image.open("random.jpg").resize((300, 100))
photo = ImageTk.PhotoImage(image)
button1 = ttk.Button(root, textvariable=buttonText, padding="10", command=printEntryInput)
quit_button = ttk.Button(root, text="End the session", command=root.destroy)
entry1 = tk.Entry(root, justify=CENTER, width=30)
hierKoennte = tk.StringVar()
hierKoennte.set("Push the button and make it happen.")
chosenList = tk.StringVar()
chosenList.set(liste_Auswahl[0])

opt = tk.OptionMenu(root, chosenList, *liste_Auswahl, command=printEntryInput)
image = Image.open("random.jpg").resize((300, 100))
photo = ImageTk.PhotoImage(image)
label4 = ttk.Label(root, image=photo)
label1 = ttk.Label(root, text = "Welcome to randomGenerator!", font=("Arial", 20))
label2 = ttk.Label(root, text="quick solutions for long morning attendance questions", font=("Arial", 12), padding=5)
label3 = ttk.Label(root, textvariable=hierKoennte, padding=20)
dummy_b = tk.Button(root, text='Try it out',command=howItWorks)

label4.pack()
label1.pack()
label2.pack()
opt.pack()
dummy_b.pack()
label3.pack() 
quit_button.pack()

root.mainloop()
