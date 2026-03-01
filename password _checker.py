import re

def check_password(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        print("❌ Password must be at least 8 characters long.")
    if uppercase_error:
        print("❌ Password must contain at least one uppercase letter.")
    if lowercase_error:
        print("❌ Password must contain at least one lowercase letter.")
    if digit_error:
        print("❌ Password must contain at least one digit.")
    if special_char_error:
        print("❌ Password must contain at least one special character.")

    if not (length_error or uppercase_error or lowercase_error or digit_error or special_char_error):
        print("✅ Strong Password!")
    else:
        print("⚠️ Weak Password. Please try again.")

if __name__ == "__main__":
    user_password = input("Enter your password to check: ")
    check_password(user_password)
