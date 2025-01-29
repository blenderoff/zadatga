import tkinter as tk
import random
import time


class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Игровой калькулятор")  #(наименование)

        self.score = 0
        self.time_left = 60
        self.current_question = ""

        self.score_label = tk.Label(master, text="Очки: 0")  #(значение очков в начале)
        self.score_label.pack()

        self.timer_label = tk.Label(master, text="Осталось времени: 60") #(начало времени)
        self.timer_label.pack()

        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Ответить", command=self.check_answer) #(кнопка ответить)
        self.submit_button.pack()

        self.start_game()

    def start_game(self):
        self.generate_question()
        self.update_timer()

    def generate_question(self):
        num1 = random.randint(1, 10)   #(1 число, выбирается рандомно)
        num2 = random.randint(1, 10)   #(2 число, выбирается рандомно)
        operation = random.choice(['+', '-'])  #(выбирается рандомно знак)

        if operation == '+':
            self.current_question = f"{num1} + {num2}"
            self.correct_answer = num1 + num2
        else:
            self.current_question = f"{num1} - {num2}"  #(функция считает либо + либо -)
            self.correct_answer = num1 - num2

        self.question_label.config(text=self.current_question)
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        try:
            answer = int(self.answer_entry.get())
            if answer == self.correct_answer:
                self.score += 1
                self.score_label.config(text=f"Очки: {self.score}")  #(добавление очков в прогресс)
            self.generate_question()
        except ValueError:
            pass  # Игнорируем некорректный ввод

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Осталось времени: {self.time_left}")  #(отсчитывает время)
            self.master.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.question_label.config(text="Игра окончена!")   #(окончание игры)
        self.answer_entry.config(state='disabled')
        self.submit_button.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()