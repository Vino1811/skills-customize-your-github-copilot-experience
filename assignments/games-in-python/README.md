## 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python that lets a player guess letters to reveal a hidden word before they run out of attempts. This assignment practices string handling, control flow, and user input.

## 📝 Tasks

### 🛠️ Implement Hangman core

#### Description
Create the main Hangman game loop that: selects a word, accepts single-letter guesses, updates and displays the current word progress, and tracks remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses and show current progress (e.g. _ a _ _ m a n)
- Track and display incorrect guesses remaining
- Prevent repeated guesses from affecting remaining attempts
- End the game when the word is fully guessed or attempts are exhausted
- Display clear win/lose messages and reveal the word on loss

### 🛠️ Optional: polish and extras (extra credit)

#### Description
Add features that improve usability or replayability.

#### Requirements (choose any)

- Add difficulty levels that change the number of allowed attempts
- Load the word list from a file (e.g., `data.csv` or a plain text file)
- Display simple ASCII hangman art as attempts are consumed
- Add input validation and helpful prompts

## Starter code

A starter file is provided at `starter-code.py` to help you begin. Use or modify it as needed.

## How to run

Run the program with Python 3:

```
python3 starter-code.py
```

## Learning outcomes

- Practice string manipulation and list operations
- Use loops and conditionals to control game flow
- Handle user input and basic error checking
