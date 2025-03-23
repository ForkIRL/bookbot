from stats import get_book_text
from stats import word_count

num_words = word_count(get_book_text("books/frankenstein.txt"))
print(f"{num_words} words found in the document")







