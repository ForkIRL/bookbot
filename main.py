from stats import get_book_text, word_counter, character_count, sort_on
import sys
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        word_count = word_counter(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at{file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    new = sort_on(character_count(book_text))
    for entry in new:
        print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")


main()



