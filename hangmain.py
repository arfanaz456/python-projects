import random
import hangmanstages

# List of words to choose from
word_list = ["apple", "beautiful", "potato"]

# Number of lives
lives = 6

# Choose a random word from the list
chosen_word = random.choice(word_list)
print(chosen_word)  # For debugging purposes, you might want to remove this in the actual game

# Initialize display with underscores
display = ['_' for _ in range(len(chosen_word))]
print(display)

game_over = False

# Main game loop
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    # Check guessed letter
    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")

    # Update display with correct guesses
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    
    # Check if guessed letter is not in the chosen word
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Incorrect guess. You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose")

    # Print the current state of the display
    print(display)

    # Check if there are no more underscores in the display
    if '_' not in display:
        game_over = True
        print("You win")

    # Print the current stage of hangman
    print(hangmanstages.stages[lives])
stages = [
    """
      ------
      |    |
      |
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    --------
    """,
    # Continue adding stages until the final state
]
