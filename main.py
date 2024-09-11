def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = character_count(text) 
    print(f"{num_words} words found in the document")
    for char, count in character_count(text).items():
        print(f"The character '{char} is found {count} times in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] =1
    return characters


main()