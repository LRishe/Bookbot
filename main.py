def main():
    with open("books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()

def word_count():
    with open("books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
        words = file_contents.split()
        word_count = len(words)
        return word_count

def character_count():
    with open("books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
        lowered = file_contents.lower()
    my_dict = {}
    for char in lowered:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

def report():
    total_words = word_count()
    with open("books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
    lowered = file_contents.lower()
    report_dict = {}
    for char in lowered:
        if char.isalpha() == True:
            if char in report_dict:
                report_dict[char] += 1
            else:
                report_dict[char] = 1
    char_list = list(report_dict.items())
    sorted_char_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")
    for char, count in sorted_char_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
report()