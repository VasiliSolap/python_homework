def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        result = []

        for ch in secret_word:
            if ch in guesses:
                result.append(ch)
            else:
                result.append("_")
        print(" ".join(result))
        return "_" not in result

    return hangman_closure

game = make_hangman("secret")

while not game(input("Guess: ")):
    pass

