# Password Complexity Checker

## Introduction
This is a Python-based **Password Complexity Checker** that evaluates the strength of user passwords and generates strong passwords if needed. It provides a user-friendly interface using **Streamlit**.

## Features
- ✅ **Check Password Strength**: Evaluates the security level of a given password.
- 🔐 **Generate Strong Passwords**: Creates secure passwords with customizable length.
- 📂 **Common Password Detection**: Prevents the use of weak, commonly used passwords.
- 🎨 **Streamlit UI**: Interactive web interface for easy use.

## Installation
Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/asutoshpanda1611/Password-Complexity-Checker.git
 cd Password-Complexity-Checker
```

### 2️⃣ Install Dependencies
Make sure you have Python installed, then run:
```sh
pip install -r requirements.txt
```
> If `requirements.txt` is not available, install manually:
```sh
pip install streamlit
```

### 3️⃣ Run the Application
```sh
streamlit run main.py
```
This will open a web-based UI in your browser.

## Usage
### **1️⃣ Check Password Strength**
- Enter a password.
- The app will analyze its strength based on length, character diversity, and common password detection.

### **2️⃣ Generate a Strong Password**
- Select a password length (8-32 characters).
- The app will generate a strong password and indicate its strength.

## File Structure
```
📂 Password-Complexity-Checker/
 ├── 📄 main.py               # Main Python script
 ├── 📄 CommonPasswords.txt   # List of common passwords
 ├── 📄 README.md             # Project documentation
```

## Contributing
Feel free to submit pull requests or report issues!

## License
This project is open-source and free to use. 🚀
