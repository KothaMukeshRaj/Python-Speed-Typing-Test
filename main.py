import time
import random
import tkinter as tk

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Typing Test")
        self.master.geometry("400x200")

        self.words = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
        self.current_word = ""
        self.user_input = ""
        self.start_time = 0
        self.elapsed_time = 0

        self.word_label = tk.Label(self.master, text=self.current_word, font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.input_entry = tk.Entry(self.master, font=("Arial", 16))
        self.input_entry.pack(pady=10)

        self.input_entry.bind("<Return>", self.check_word)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        self.user_input = ""
        self.input_entry.delete(0, "end")
        self.input_entry.focus()

        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word, fg="black")

        self.start_time = time.time()

    def check_word(self, event):
        self.user_input = self.input_entry.get()

        if self.user_input == self.current_word:
            self.word_label.config(fg="green")
        else:
            self.word_label.config(fg="red")

        self.elapsed_time = time.time() - self.start_time
        self.show_results()

    def show_results(self):
        wpm = len(self.user_input.split()) / (self.elapsed_time / 60)
        accuracy = sum([1 for i in range(len(self.user_input)) if self.user_input[i] == self.current_word[i]]) / len(self.user_input) * 100

        result_text = f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"

        result_label = tk.Label(self.master, text=result_text, font=("Arial", 16))
        result_label.pack(pady=10)

        self.start_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    speed_test = SpeedTypingTest(root)
    root.mainloop()
