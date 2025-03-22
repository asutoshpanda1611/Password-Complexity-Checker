import string
import random
import streamlit as st

class Password:
    def check_password_strength(self, password):
        if not password:
            st.error("Password cannot be empty!")
            return
        
        length = len(password)
        upper_case = any(c.isupper() for c in password)
        lower_case = any(c.islower() for c in password)
        specialchar = any(c in string.punctuation for c in password)
        digits = any(c.isdigit() for c in password)

        char_types = sum([upper_case, lower_case, specialchar, digits])
        score = 0

        try:
            with open('CommonPasswords.txt', 'r') as f:
                for line in f:
                    if password == line.strip():
                        st.error("Password is too common! Score: 0 / 7")
                        return
        except FileNotFoundError:
            st.warning("'CommonPasswords.txt' not found")

        if length > 8: score += 1
        if length > 12: score += 1
        if length > 17: score += 1
        if length > 20: score += 1       
        st.info(f"Password length: {length}, adding {score} points.")

        if char_types > 1: score += 1
        if char_types > 2: score += 1
        if char_types > 3: score += 1
        st.info(f"Password contains {char_types} different character types, adding {char_types - 1} points.")

        if score < 4:
            st.error(f"Weak password! Score: {score} / 7")
        elif score == 4:
            st.warning(f"Okay password! Score: {score} / 7")
        elif 4 < score < 7:
            st.success(f"Pretty strong password! Score: {score} / 7")
        elif score == 7:
            st.success(f"Very strong password! Score: {score} / 7")

    def generate_strong_password(self, length=16):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""  
        for i in range(length):  
            password += random.choice(characters)  
        return password

st.markdown(
    "<h1 style='text-align: center; margin-top: -30px;'>Password Strength Checker & Generator</h1>", 
    unsafe_allow_html=True
)

passw = Password()

option = st.radio("Choose an option:", ["Check Password Strength", "Generate Strong Password"])

if option == "Check Password Strength":
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Strength"):
        passw.check_password_strength(password)

elif option == "Generate Strong Password":
    length = st.slider("Select password length:", min_value=5, max_value=32, value=16)

    if st.button("Generate"):
        strong_password = passw.generate_strong_password(length)
        
        if length < 10:
            strength = "Weak"
            color = "red"
        elif 10 <= length < 14:
            strength = "Okay"
            color = "orange"
        elif 14 <= length < 20:
            strength = "Strong"
            color = "blue"
        else:
            strength = "Very Strong"
            color = "green"
        
        st.success(f"Generated Password: `{strong_password}`")
        st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
