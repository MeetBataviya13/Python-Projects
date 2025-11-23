import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="Stone Paper Scissors", page_icon="🎮", layout="centered")
st.title("🪨 Stone - 📄 Paper - ✂️ Scissors Game")
st.write("Play against the computer! First to reach 5 points wins the match 🏆")

# --- SESSION STATE (to keep score persistent) ---
if "hscore" not in st.session_state:
    st.session_state.hscore = 0
if "cscore" not in st.session_state:
    st.session_state.cscore = 0
if "message" not in st.session_state:
    st.session_state.message = ""
if "com_choice" not in st.session_state:
    st.session_state.com_choice = ""

# --- CHOICES ---
choices = {1: "🪨 Stone", 2: "📄 Paper", 3: "✂️ Scissors"}

# --- GAME LOGIC ---
def play_game(user_choice):
    com = random.randint(1, 3)
    st.session_state.com_choice = choices[com]

    if user_choice == com:
        st.session_state.message = "It's a draw 🤝"
    elif (user_choice == 1 and com == 3) or \
         (user_choice == 2 and com == 1) or \
         (user_choice == 3 and com == 2):
        st.session_state.hscore += 1
        st.session_state.message = "You won this round! 🏅"
    else:
        st.session_state.cscore += 1
        st.session_state.message = "Computer won this round 👿"

# --- RESET FUNCTION ---
def reset_game():
    st.session_state.hscore = 0
    st.session_state.cscore = 0
    st.session_state.message = ""
    st.session_state.com_choice = ""

# --- BUTTONS FOR USER CHOICE ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Stone"):
        play_game(1)
with col2:
    if st.button("📄 Paper"):
        play_game(2)
with col3:
    if st.button("✂️ Scissors"):
        play_game(3)

# --- DISPLAY COMPUTER CHOICE ---
if st.session_state.com_choice:
    st.write(f"**Computer chose:** {st.session_state.com_choice}")

# --- SCORES ---
st.subheader(f"🏅 You: {st.session_state.hscore} 💻 Computer: {st.session_state.cscore}")

# --- RESULT MESSAGE ---
if st.session_state.message:
    st.info(st.session_state.message)

# --- WINNING CONDITION ---
if st.session_state.hscore == 5:
    st.success("🎉 Congratulations! You won the game!")
    reset_game()

elif st.session_state.cscore == 5:
    st.error("💻 Computer won the game! Better luck next time!")
    reset_game()

# --- RESET BUTTON ---
st.button("🔄 Reset Game", on_click=reset_game)
