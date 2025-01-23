
def main():
    print("1. Frankenstein")
    print("2. Moby-Dick")
    print("3. The Great Gatsby")
    print("4. Notes From Underground")
    print("5. War and Peace")
    user_input = int(input("Please enter the number of your desired book.\n"))

    if user_input == 1:
        print("You selected: Frankenstein by Mary Shelley")
        book = "frankenstein"
    elif user_input == 2:
        print("You selected: Moby-Dick by Herman Melville")
        book = "moby_dick"
    elif user_input == 3:
        print("You selected: The Great Gatsby by F. Scott Fitzgerald")
        book = "the_great_gatsby"
    elif user_input == 4:
        print("You selected: Notes From Underground by Fyodor Dostoevsky")
        book = "notes_from_underground"
    elif user_input == 5:
        print("You selected: War and Peace by Leo Tolstoy")
        book = "war_and_peace"
    else:
        print("Please enter a number 1-5")

    read_file(book)
    
    print("1. Publication info")
    print("2. Word and character count")
    print("3. Full text")
    user_input2 = int(input("\nWhat would you like to see?\n"))


    if user_input2 == 1:
        print(read_file(f"/publication_info/{book}_publication_info"))
    elif user_input2 == 2:
        report(book)
    elif user_input2 == 3:
        print(read_file(book))
    
        
 

def read_file(book):
    with open(f"books/{book}.txt") as name:
        file_contents = name.read()
        return file_contents

def word_count(book):
    words = read_file(book).split()
    word_count = len(words)
    return word_count

def character_count(book):
    lowered = read_file(book).lower()
    my_dict = {}
    for char in lowered:
        if char in my_dict and char.isalpha() == True:
            my_dict[char] += 1
        elif char not in my_dict and char.isalpha() == True:
            my_dict[char] = 1
    return my_dict

def report(book):
    total_words = word_count(book)
    lowered = read_file(book).lower()
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

if __name__ == "__main__":
    main()
