# J-D Laurence

# Task 4

# Declare a function called make_hangman() that has one argument called secret_word.
# It should also declare an empty array called guesses. Within the function declare
# a function called hangman_closure() that takes one argument, which should be a letter.
# Within the inner function, each time it is called, the letter should be appended 
# to the guesses array. Then the word should be printed out, with underscores
# substituted for the letters that haven't been guessed. So, if secret_word
#  is "alphabet", and guesses is ["a", "h"], then "a__ha___" should be printed out.
# The function should return True if all the letters have been guessed,
# and False otherwise. make_hangman() should return hangman_closure.

#initial attempt
# def make_hangman(secret_word):
#     guesses = []
#     def hangman_closure(guess):
#         guesses.append(guess)
#         char_list = list(secret_word)
#         for i, ch in enumerate(char_list):
#             if ch not in guesses: char_list[i] = '_'
#         latest = "".join(char_list)
#         print(latest)
#         return latest == secret_word
#     return hangman_closure

#better is
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(guess):
        guesses.append(guess)
        output_word = "".join([ch if ch in guesses else "_" for ch in secret_word]) #list comprehension
        print(output_word)
        return output_word == secret_word
    return hangman_closure

print("Let's play Hangman!")
secret = input("Enter the secret word: ")
game = make_hangman(secret.lower())
solved = False
while not solved:
    guess = input("Guess a letter: ")
    solved = game(guess.lower())
print("Congratulations!")

