
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. By the end of this assignment, students should be able to manage game state and control flow in an interactive console program.

## 📝 Tasks

### 🛠️ Implement the Core Hangman Loop

#### Description
Create the game flow for Hangman: choose a hidden word, receive letter guesses from the player, reveal correct letters, and reduce remaining attempts for incorrect guesses.

#### Requirements
O programa concluído deve:

- Select a random word from a predefined list.
- Display the current progress using underscores for hidden letters (for example: `_ _ _ _ _`).
- Accept one letter per turn and update the visible word when the guess is correct.
- Track and display remaining incorrect attempts.
- End the game when the player guesses the full word or runs out of attempts.

### 🛠️ Improve Validation and Player Feedback

#### Description
Add input validation and clear feedback messages to make the game easier to play and understand.

#### Requirements
O programa concluído deve:

- Reject invalid input (empty input, more than one character, non-letter characters).
- Warn the player when a letter has already been guessed.
- Display a clear win message with the discovered word.
- Display a clear loss message with the correct word when attempts reach zero.