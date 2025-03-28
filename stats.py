def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def word_count(book_text):
    amount = len(book_text.split())
    return amount
def character_count(book_text):
    character_dic = dict()
    for i in range(len(book_text)):
        character = book_text[i].lower()
        if character in character_dic:
            character_dic[character] += 1
        else:
            character_dic[character] = 1
    return character_dic
