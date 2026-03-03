import re

# Load common passwords from file
def load_common_passwords(filename="common.txt"):
    try:
        with open(filename, "r") as f:
            # Strip newlines and convert to lowercase
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"⚠️ Warning: {filename} not found. Skipping common password check.")
        return set()

def check_password(password, common_passwords):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    common_password_error = password.lower() in common_passwords

    # Strength score calculation
    score = 0
    if not length_error:
        score += 1
    if not uppercase_error:
        score += 1
    if not lowercase_error:
        score += 1
    if not digit_error:
        score += 1
    if not special_char_error:
        score += 1
    if common_password_error:
        score = 0  # Common password = automatically weakest

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
    if common_password_error:
        print("❌ Password is too common. Avoid easy passwords!")

    # Strength display
    print(f"\n🔎 Strength Score: {score}/5")

    if score == 5:
        print("💪 Very Strong Password!")
    elif score == 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password.")
    elif score == 2:
        print("⚠️ Weak Password.")
    else:
        print("❌ Very Weak Password.")

if __name__ == "__main__":
    common_passwords = load_common_passwords("common.txt")
    user_password = input("Enter your password to check: ")
    check_password(user_password, common_passwords)
