from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("LANGUAGE TRANSLATOR")
root.geometry("1000x500")
root.config(bg="#F2CCC3")

languages = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=languages, state="readonly", width=20)
src_lang.place(relx=0.2, rely=0.25, anchor=W)
src_lang.set("english")


title_label = Label(root, text="LANGUAGE TRANSLATOR", bg="#F2CCC3", font=("Constantia", 20, "bold"))
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

enter_text_label = Label(root, text="Enter Text :", bg="#F2CCC3", font=("Constantia", 15))
enter_text_label.place(relx=0.05, rely=0.25, anchor=W)

textarea = Text(root, bg="white", font=("Arial", 12, "normal"), height=10, wrap=WORD, width=40, padx=5, pady=5, bd=0)
textarea.place(relx=0.05, rely=0.5, anchor=W)

output_label = Label(root, text="Output : ", bg="#F2CCC3", font=("Constantia", 15))
output_label.place(relx=0.7, rely=0.25, anchor=W)

output_lang_combobox = ttk.Combobox(root, values=languages, state="readonly", width=20)
output_lang_combobox.place(relx=0.8, rely=0.25, anchor=W)
output_lang_combobox.set("Choose output language")

converted_textarea = Text(root, bg="white", font=("Arial", 12, "normal"), height=10, wrap=WORD, width=40, padx=5, pady=5, bd=0)
converted_textarea.place(relx=0.58, rely=0.5, anchor=W)



creatorlabel = Label(root, text="Created by Sam", font=("Constantia", 12, "normal"), bg="lightpink", fg="black")
creatorlabel.place(relx = 0.5, rely=0.95)

def Translate():
    translator = Translator()

    try:
        s_lang = src_lang.get()
        out_lang = output_lang_combobox.get()
        tr_text = textarea.get(1.0, END)
        translated = translator.translate(text=tr_text, src=s_lang, dest=out_lang)

        converted_textarea.insert(END, translated.text)
    
    except:
        print("Error, try again!")


translate_button = Button(root, text="Translate", command=Translate, font=("Constantia", 12, "normal"), bg="lightpink", activebackground="#A2A4C2", fg="black", relief=FLAT, pady=5)
translate_button.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()