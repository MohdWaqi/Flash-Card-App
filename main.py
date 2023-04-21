from tkinter import *
import pandas
import random
try:
    data = pandas.read_csv("data/words_not_known.csv")
except FileNotFoundError:
    data_original = pandas.read_csv("data/English.csv")
    word_list = data_original.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(language_title, text="Meaning", fill="brown")
    canvas.itemconfig(language_word, width=750, text=f"{current_word['Hindi Meaning']}", fill="White")


def next_card():
    global current_word
    current_word = random.choice(word_list)
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(language_title, text="English", fill="orange")
    canvas.itemconfig(language_word, text=f"{current_word['Word']}", fill="blue")
    window.after(3000, flip_card)


def is_known():
    word_list.remove(current_word)
    words_to_learn = pandas.DataFrame(word_list)
    words_to_learn.to_csv("data/words_not_known.csv", index=False)
    next_card()


def not_clear():
    doubt_list = []
    doubt_list.append(current_word)
    doubt_words = pandas.DataFrame(doubt_list)
    doubt_words.to_csv("data/doubted_Words.csv", mode="a", index=False, header=False)
    next_card()


window = Tk()
window.title("English Words")
window.config(bg="yellow", padx=50, pady=50)
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_image)
canvas.config(bg="yellow", highlightthickness=0)
language_title = canvas.create_text(400, 150, text="English", font=("Arial", 40, "normal"))
language_word = canvas.create_text(400, 300, text="word", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=3)
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=is_known)
right_button.grid(row=1, column=0)
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=next_card)
wrong_button.grid(row=1, column=2)
doubt = Button(text="Doubt", width=10, height=2, font=("arial", 20, "bold"), bg="purple", command=not_clear)
doubt.grid(row=1, column=1)
next_card()
window.mainloop()