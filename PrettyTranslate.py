from pynput import keyboard
from pyperclip import paste
import tkinter as tk
from googletrans import Translator
from tkinter import messagebox as msg

class ceviri(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Çeviri Penceresi")
        self.geometry("400x200")
        pano = paste()

        self.cevirilecek = tk.Entry()
        self.cevirilecek.insert(0, pano)
        self.cevirilecek.pack()

        tk.Label(text="Hangi dile çevirilecek? (Yalnızca kısaltmasını girin)").pack()

        self.neye = tk.Entry()
        self.neye.insert(0, "tr")
        self.neye.pack()

        tk.Button(text="Çevir", command=self.cevir).pack()

    def cevir(self):
        c = self.cevirilecek.get()

        try:
            trnsl = Translator()
            ceviri = trnsl.translate(c, dest = self.neye.get()).text

            msg.showinfo("Çeviri başarılı", "Çeviri:\n"+ceviri)
            self.destroy()
        except:
            msg.showerror("Hata", "Dil kısaltmasını hatalı girdiniz, lütfen yeniden deneyin.")

def on_press(key):
    if key == keyboard.Key.ctrl:
        pen = ceviri()
        pen.mainloop()

with keyboard.Listener(on_press=on_press) as ls:
    ls.join()
        
