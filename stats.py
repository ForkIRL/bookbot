def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def word_count(book_text):
    amount = len(book_text.split())
    return amount