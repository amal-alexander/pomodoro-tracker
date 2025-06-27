import streamlit as st
import time
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Optional: Local sound
try:
    from playsound import playsound
    SOUND_ENABLED = True
except ImportError:
    SOUND_ENABLED = False

# Load email credentials
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Email sending function
def send_email(subject, body, to):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print("❌ Email send error:", e)

# Main timer function (no threading — live UI updates)
def pomodoro_session(task_name, email, break_enabled):
    total_seconds = 25 * 60
    emoji_cycle = ["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"]
    quotes = [
        "💡 Stay focused. Your future self will thank you.",
        "📵 Ignore distractions. Just this session.",
        "🎯 Deep work = real progress.",
        "💪 You got this. One block at a time.",
        "✨ Small steps make big impact."
    ]

    ph = st.empty()

    for sec in range(total_seconds, -1, -1):
        mins, secs = divmod(sec, 60)
        emoji = emoji_cycle[sec % len(emoji_cycle)]
        quote = quotes[(total_seconds - sec) % len(quotes)]
        percent = (total_seconds - sec) / total_seconds

        # Render content
        with ph.container():
            st.markdown(f"<h2 style='text-align:center;'>⏳ {mins:02d}:{secs:02d}</h2>", unsafe_allow_html=True)

            progress_bar_html = f"""
                <div style='width:100%; background:#ddd; border-radius:10px; height:20px;'>
                    <div style='width:{int(percent*100)}%; background:#4CAF50; height:100%; border-radius:10px; transition: width 0.2s;'></div>
                </div>
            """
            st.markdown(progress_bar_html, unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:60px; text-align:center;'>{emoji}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; text-align:center;'>{quote}</p>", unsafe_allow_html=True)

        time.sleep(1)

    # After timer ends
    if SOUND_ENABLED:
        try:
            playsound("alarm.mp3")
        except Exception as e:
            print("🔇 Sound error:", e)

    st.success(f"🎉 Pomodoro complete for: **{task_name}**")
    send_email("✅ Pomodoro Complete", f"Task '{task_name}' is complete. Take a break!", email)

    if break_enabled:
        st.info("🛌 Starting 5-minute break...")
        for sec in range(5 * 60, -1, -1):
            mins, secs = divmod(sec, 60)
            st.metric("🧘 Break Time Remaining", f"{mins:02d}:{secs:02d}")
            time.sleep(1)
        st.success("🔔 Break done! Time for your next session.")

# UI Setup
st.set_page_config(page_title="🍅 Pomodoro Tracker", layout="centered")
st.title("🍅 Pomodoro Task & Time Tracker")

task = st.text_input("📝 Enter your task")
user_email = st.text_input("📧 Email for session-end alert")
take_break = st.checkbox("Take a 5-minute break after session?", value=True)

if st.button("▶️ Start Pomodoro"):
    if task and user_email:
        pomodoro_session(task, user_email, take_break)
    else:
        st.warning("⚠️ Enter both task name and your email.")
