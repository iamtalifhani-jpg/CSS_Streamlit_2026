import streamlit as st
import random

st.set_page_config(page_title="Valentine App", layout="centered")

st.title("💌 Will you be my Valentine?")

# Session state to track button position changes
if "no_pos" not in st.session_state:
    st.session_state.no_pos = random.randint(0, 2)

if "answered" not in st.session_state:
    st.session_state.answered = False

# Function to move the NO button
def move_no():
    st.session_state.no_pos = random.randint(0, 2)

# Layout with 3 columns so the NO button can "jump"
cols = st.columns(3)

# YES button (always center column)
with cols[1]:
    if st.button("💖 YES 💖", use_container_width=True):
        st.session_state.answered = True
        st.balloons()

# NO button appears in a random column each time
with cols[st.session_state.no_pos]:
    if st.button("🙈 NO 🙈", key="no_button", use_container_width=True):
        move_no()
        st.warning("Oh no you don’t 😜 Try again!")

# Celebration after YES
if st.session_state.answered:
    st.success("Yaaay!! You made my day! 💕")
    st.write("❤️ 💖 💘 💝 💓 💗 💞 💕")
    st.write("You are officially my Valentine! 🌹")
