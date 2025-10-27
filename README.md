## Project : Password Strength Analyzer with Custom Wordlist Generator

An intelligent Python-based password analysis and awareness tool with automatic wordlist generation — built for cybersecurity education.”

# 🔐 Smart Password Strength Analyzer with Custom Wordlist Generator

**Author:** Faiza Maniar  
**Domain:** Cybersecurity | Python | Password Security  
**Project Type:** Internship Project (2025)  


## Overview

The **Smart Password Strength Analyzer** is a Python-based cybersecurity tool designed to evaluate password strength using real-world entropy analysis (zxcvbn) and generate personalized wordlists for awareness and testing purposes.
It helps users understand how predictable personal details (like names, pets, or years) can weaken their passwords — a key aspect of cybersecurity training.


## Objective : Build a tool to analyze password strength and generate custom wordlists.

- Analyze password strength using advanced scoring methods.  
- Educate users on password creation and vulnerabilities.  
- Generate a custom wordlist for ethical testing and awareness.  
- Export detailed reports and wordlists automatically.


## Features
- **Advanced Strength Analysis** | Uses `zxcvbn` to calculate password entropy and crack time. |
- **Custom Scoring** | Additional readability score based on character variety and length. |
- **Color-Coded Feedback** | Visual CLI output for quick understanding. |
- **Wordlist Generator** | Builds a personalized wordlist from user input (name, pet, year). |
- **File Export System** | Automatically saves `password_report.txt` and `custom_wordlist.txt`. |


##  Tools & Libraries Used

- **Language:** Python 3.12.4  
- **Libraries:**  
  - `zxcvbn` → password strength analysis  
  - `itertools`, `os`, `datetime` → wordlist and file management  
- **Editor:** Visual Studio Code  


##  How to Run the Project

**Step 1** Install Dependencies
      pip install zxcvbn-python

**Step 2** Run the Program

**Step 3** Choose from Menu
  1. Check password strength
  2️. Generate custom wordlist
  3️. Exit

**Step 4** Output Files
  - password_report.txt → stores password evaluation results
  - custom_wordlist.txt → contains generated words for awareness

## Deliverables: Tool that evaluates password strength and exports attack-specific wordlists.

## Screenshots 
1. Code Running
2. Password check
3. Wordlist created
4. Custom wordlist

**Future Improvements**
- Add a simple GUI using Tkinter.
- Visual charts for password statistics.
- Integration with web password audit tools.

## Project Selection

I selected this project because password **security** is a core part of **cybersecurity** awareness. My tool combines both strength analysis and custom wordlist generation to show users how personal data can weaken passwords.It’s functional, easy to use, and helps demonstrate real password vulnerability concepts.
