# Smart Password Strength Analyzer with Custom Wordlist Generator
# Author: Faiza Maniar
# Goal: To create a password strength analyzer that's simple, colorful, and unique.

from zxcvbn import zxcvbn
import itertools
import datetime
import os

# ----- Color codes for console output -----
class color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# ----- Password Strength Analyzer -----
def analyze_password(password):
    print("\n🔍 Analyzing password strength...\n")
    result = zxcvbn(password)
    score = result['score']
    strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    strength = strength_levels[score]

    # Custom readability check (unique addition)
    custom_points = 0
    if any(c.isupper() for c in password): custom_points += 1
    if any(c.islower() for c in password): custom_points += 1
    if any(c.isdigit() for c in password): custom_points += 1
    if any(c in "!@#$%^&*()" for c in password): custom_points += 1
    if len(password) >= 12: custom_points += 1

    print(color.CYAN + f"Password: {password}" + color.RESET)
    if score <= 1:
        color_used = color.RED
    elif score == 2:
        color_used = color.YELLOW
    else:
        color_used = color.GREEN
    print(color_used + f"Strength: {strength} ({score}/4)" + color.RESET)
    print(f"Custom score: {custom_points}/5 (based on variety and length)")
    print("Guesses (log10):", result['guesses_log10'])
    print("Crack Time:", result['crack_times_display']['offline_slow_hashing_1e4_per_second'])
    print("Feedback:", result['feedback']['warning'] or "Looks good!")

    # Save report
    import os
    report_path = os.path.join(os.path.dirname(__file__), "password_report.txt")
    with open(report_path, "w") as f:

        f.write(f"Password: {password}\nStrength: {strength}\nCustom score: {custom_points}/5\n")
        f.write(f"Crack time: {result['crack_times_display']}\n")
        f.write(f"Feedback: {result['feedback']}\n")
    print("\n Detailed report saved as 'password_report.txt'")

# ----- Custom Wordlist Generator -----
def generate_wordlist():
    print("\nLet's generate your custom wordlist!")
    name = input("Enter your name: ").lower()
    pet = input("Enter your pet's name (optional): ").lower()
    year = input("Enter a memorable year or number: ")

    words = [w for w in [name, pet, year] if w]
    wordlist = set()

    for combo in itertools.permutations(words, 2):
        base = ''.join(combo)
        wordlist.add(base)
        wordlist.add(base + "123")
        wordlist.add(base + "@2024")
        wordlist.add(base.capitalize())
        wordlist.add(base[::-1])  # reversed word (unique addition)

    wordlist_path = os.path.join(os.path.dirname(__file__), "custom_wordlist.txt")
    with open(wordlist_path, "w") as file:

        for w in sorted(wordlist):
            file.write(w + "\n")

    print(color.GREEN + f"\nWordlist created successfully! ({len(wordlist)} entries)" + color.RESET)
    print("Saved as 'custom_wordlist.txt'")

# ----- Main menu -----
def main():
    print(color.CYAN + "\n========== SMART PASSWORD ANALYZER ==========" + color.RESET)
    print("1️ : Check password strength")
    print("2️ : Generate custom wordlist")
    print("3️ : Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        pw = input("Enter a password to check: ")
        analyze_password(pw)
    elif choice == "2":
        generate_wordlist()
    else:
        print("You have a secure day ahead:)!")

if __name__ == "__main__":
    main()
    