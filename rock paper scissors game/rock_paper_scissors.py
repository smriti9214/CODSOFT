import random 
import tkinter as tk

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")

emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

choices = ["rock", "paper", "scissors"]
user_score=0
computer_score=0

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score: You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady = 10)

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    result_label.config(
    text=f"You: {emoji[user_choice]} | Computer: {emoji[computer_choice]}\n{result}"
)
    score_label.config(text=f"Score: You: {user_score} | Computer: {computer_score}")


title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
title.pack(pady=10)

btn_rock = tk.Button(root, text="🪨", width=10, command = lambda: play("rock"))
btn_paper = tk.Button(root, text="📄", width=10, command = lambda: play("paper"))
btn_scissors= tk.Button(root, text="✂️", width=10, command = lambda: play("scissors"))
btn_rock.pack(pady=5)
btn_paper.pack(pady=5)
btn_scissors.pack(pady=5)

root.mainloop()