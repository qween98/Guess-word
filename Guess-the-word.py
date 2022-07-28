import tkinter as tk
import tkinter.messagebox as tmb
import random
window = tk.Tk()
window.title("Угадай слово")
window.geometry("300x200")
with open("words.txt") as file:
    data = file.read()
words = data.split()
word = random.choice(words)
letters = []
def check_letter():
    global letter, word
    letter = entry_letter.get()
    letters.append(letter)
    entry_letter.delete(0, "end")
    print(letters)
    show_word = ""
    for char in word:
        if char in letters:
            show_word += char
        else:
            show_word += "*"       

    label_word["text"] = show_word
  
    if show_word == word:
        print("Победа")
        tmb.showinfo("Победа", "Ты угадал слово!")
        new_game()
        
        
        


label_word = tk.Label(window, text = "Здесь будет слово", font = ("Arial", 15))
label_word.place(x = 70, y = 20)
entry_letter = tk.Entry(window, width = 8, font = ("Arial", 10))
entry_letter.place(x = 130, y = 80)
check_button = tk.Button(window, text = "Проверить букву", font = ("Arial", 10), command = check_letter)
check_button.place(x = 100, y = 120)


def new_game():
    global letters
    global word
    letters = []
    with open("words.txt") as file:
        data = file.read()
    words = data.split()
    word = random.choice(words)
     
             
    





















window.mainloop()
