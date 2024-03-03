import random

letter_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

letters = [letter for letter in letter_values for _ in range(4)]
random.shuffle(letters)

def draw_tiles(num_tiles):
    tiles = []
    for _ in range(num_tiles):
        if letters:
            tiles.append(letters.pop())
        else:
            print("No more tiles left!")
            break
    return tiles

def calculate_score(word):
    score = 0
    for letter in word:
        score += letter_values.get(letter.upper(), 0)
    return score

def play_scrabble():
    player_score = 0
    tiles = draw_tiles(7)

    print("Welcome to Scrabble!")
    print("Your tiles are:", tiles)

    while True:
        word = input("Enter a word (or 'q' to quit): ")
        if word.lower() == 'q':
            break
        
        if all(letter.upper() in tiles for letter in word) and len(word) > 1:
            score = calculate_score(word)
            print(f"Score for '{word}': {score}")
            player_score += score
            print("Total score:", player_score)
            for letter in word:
                tiles.remove(letter.upper())
            new_tiles = draw_tiles(len(word))
            tiles.extend(new_tiles)
            print("Your new tiles are:", tiles)
        else:
            print("Invalid word. Make sure it can be formed with your tiles.")

    print("Thanks for playing! Final score:", player_score)

play_scrabble()
