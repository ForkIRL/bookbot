def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def word_count(book_text):
    amount = len(book_text.split())
    return amount


num_words = word_count(get_book_text("books/frankenstein.txt"))
print(f"{num_words} words found in the document")







