import re
import streamlit as st

if "password_history" not in st.session_state:
    st.session_state.password_history = []

def check_password_strength(password):
    """Checks password strength and returns score & feedback."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def store_password(password, score):
    history = st.session_state.password_history

    
    if score == 5:
        if any(password == old_pass for old_pass in history[-3:]):
            return "⚠️ This password is similar to one of your last 3 passwords. Consider changing it."
        
        history.append(password)
        if len(history) > 10:
            history.pop(0)  

        st.session_state.password_history = history
        return None 

    return None 

st.title("🔐 Password Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    warning = store_password(password, score) 

    with st.container():  
        if score <= 2:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
            strength_label = "Weak"
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            strength_label = "Moderate"
        else:
            st.success("✅ Strong Password!")
            strength_label = "Strong"

        st.markdown(f"**Strength Level: {strength_label}**")
        st.progress(score / 5)

    if warning:
        st.warning(warning)

    with st.container():
        for msg in feedback:
            st.error(msg)

with st.expander("🔍 View Last 10 Passwords"):
    if st.session_state.password_history:
        st.markdown("**🔹 Your Recent Passwords:**")
        st.markdown("\n".join([f"- {pwd}" for pwd in st.session_state.password_history]))
    else:
        st.info("No strong passwords stored yet. Create one!")

