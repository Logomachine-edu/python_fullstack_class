while True:
    word: str = input()
    middle: int = int(len(word) / 2)
    print(f'{word[middle:]}{word[:middle]}')