from stats import get_book_text
from stats import word_counter
from stats import character_count
from stats import sort_on
file_path = "books/frankenstein.txt"
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






