import streamlit as st
import re

# --- Functions ---
def password_strength(password):
    strength = 0
    suggestions = []

    if len(password) < 6:
        suggestions.append("Password should be at least 6 characters.")
    else:
        strength += 1

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make it longer than 8 characters for extra safety.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one UPPERCASE letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Include numbers (0-9).")

    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1
    else:
        suggestions.append("Use special characters like !, @, #, etc.")

    return strength, suggestions

def strength_feedback(strength):
    if strength == 0:
        return "Very Weak 😡", "red"
    elif strength == 1:
        return "Weak 😞", "orangered"
    elif strength == 2:
        return "Fair 😐", "orange"
    elif strength == 3:
        return "Good 🙂", "yellowgreen"
    elif strength == 4:
        return "Strong 😎", "green"
    elif strength == 5:
        return "Very Strong 🚀", "darkgreen"

# --- Streamlit Page ---
st.set_page_config(page_title="Pro Password Strength Meter", page_icon="🔒", layout="centered")

# ---- HEADER WITH YOUR INFO ----
st.markdown(
    """
    <div style='text-align: center;'>
        <h1>🔒 Pro Password Strength Meter</h1>
        <h4>by <a href="https://github.com/Mr-NOMAN-RAJAR" style="text-decoration: none;" target="_blank">Noman</a> 👨‍💻</h4>
        <p>Frontend Developer | Web Designer | Tech Enthusiast 🚀</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Custom Style for Progress Bar ---
st.markdown(
    """
    <style>
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00b4db, #0083b0);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- MAIN FUNCTIONALITY ---
password = st.text_input("Enter your password:", type="password", help="We never store your password.")

if password:
    strength, suggestions = password_strength(password)
    percent = (strength / 5) * 100
    feedback, color = strength_feedback(strength)

    # Progress bar
    st.progress(percent / 100)

    # Feedback Message
    st.markdown(f"<h3 style='color:{color};'>{feedback}</h3>", unsafe_allow_html=True)

    # Suggestions
    if suggestions:
        st.subheader("🔎 Suggestions to improve:")
        for suggestion in suggestions:
            st.write(f"👉 {suggestion}")
    else:
        st.success("✅ Your password is super strong!")

else:
    st.info("👆 Start typing a password to see the magic!")

# ---- FOOTER ----
st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
        Made with ❤️ by <a href="https://www.linkedin.com/in/noman-rajar-5351bb2b4/" target="_blank" style="text-decoration: none;">Noman</a> | 
        <a href="https://noman-portfolioweb.vercel.app/" target="_blank" style="text-decoration: none;">Portfolio</a>
    </div>
    """,
    unsafe_allow_html=True,
)
