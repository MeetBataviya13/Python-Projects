import tkinter as tk
import random
from tkinter import messagebox

# Main window setup
root = tk.Tk()
root.title("Stone Paper Scissors Game")
root.geometry("400x400")
root.config(bg="#1e1e1e")

# Scores
cscore = 0
hscore = 0

# Functions
def play(user_choice):
    global cscore, hscore
    choices = {1: "Stone", 2: "Paper", 3: "Scissors"}
    com_choice = random.randint(1, 3)
    
    result_label.config(text=f"Computer chose: {choices[com_choice]}")

    if user_choice == com_choice:
        outcome = "It's a draw 🤝"
    elif (user_choice == 1 and com_choice == 3) or \
         (user_choice == 2 and com_choice == 1) or \
         (user_choice == 3 and com_choice == 2):
        hscore += 1
        outcome = "You won this round! 🏅"
    else:
        cscore += 1
        outcome = "Computer won this round 👿"
    
    score_label.config(text=f"You: {hscore}   Computer: {cscore}")
    result_label2.config(text=outcome)

    # Check for winner
    if hscore == 5:
        messagebox.showinfo("Game Over", "🎉 Congratulations! You Won!")
        reset_game()
    elif cscore == 5:
        messagebox.showinfo("Game Over", "💻 Computer Won! Better Luck Next Time!")
        reset_game()

def reset_game():
    global cscore, hscore
    cscore = 0
    hscore = 0
    score_label.config(text="You: 0   Computer: 0")
    result_label.config(text="")
    result_label2.config(text="")

# UI Elements
title = tk.Label(root, text="🪨 Stone - 📄 Paper - ✂️ Scissors", 
                 font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00ff99")
title.pack(pady=10)

score_label = tk.Label(root, text="You: 0   Computer: 0", 
                       font=("Arial", 14), bg="#1e1e1e", fg="white")
score_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e", fg="white")
result_label.pack(pady=5)

result_label2 = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#1e1e1e", fg="#00ffcc")
result_label2.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

stone_btn = tk.Button(button_frame, text="🪨 Stone", width=12, height=2, bg="#333", fg="white",
                      command=lambda: play(1))
stone_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, height=2, bg="#333", fg="white",
                      command=lambda: play(2))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, height=2, bg="#333", fg="white",
                         command=lambda: play(3))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(root, text="🔄 Reset Game", width=15, height=2, bg="#444", fg="white",
                      command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
