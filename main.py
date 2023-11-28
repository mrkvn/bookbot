filepath = "books/frankenstein.txt"
with open(filepath, encoding="utf-8") as f:
    file_contents = f.read()
    words = file_contents.split()
    count_letters = {}
    for letter in file_contents:
        if letter.lower() in count_letters:
            count_letters[letter.lower()] += 1
        else:
            count_letters[letter.lower()] = 1
    count_letters_list = []
    for k in count_letters:
        count_letters_list.append({"char": k, "count": count_letters[k]})
    count_letters_list.sort(key=lambda x: x["count"], reverse=True)
    print(f"--- Begin report of {filepath} ---")
    print(f"{len(words)} words found in the document")
    print()
    for i in count_letters_list:
        if i["char"].isalpha():
            print(f"The '{i['char']}' character was found {i['count']} times")
    print("--- End report ---")
