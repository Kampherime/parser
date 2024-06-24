import sys

def main():
    with open(sys.argv[1]) as f:
        word_list = split_file(f)
        word_count = get_wc(word_list)
        gen_report(create_dict(word_list), word_count, sys.argv[1])

def create_dict(word_list):
    book_string = " ".join(word_list)
    lowercase_string = book_string.lower()
    letter_dict = {}
    for letter in lowercase_string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def get_wc(split_file):
    return len(split_file)

def split_file(file):
    file_contents = file.read()
    return file_contents.split()


def sort_on(dictionary):
    return dictionary["num"]
        

def gen_report(letter_dict, word_count, novel):
    dict_value_list = list(letter_dict.values())
    dict_key_list = list(letter_dict.keys())
    dict_list = []

    for i in range(0, len(dict_key_list)):
        dict_list.append({"name": dict_key_list[i], "num":dict_value_list[i]})

    dict_list.sort(reverse=True, key=sort_on)

    print("------Start report------")
    print(f"There are {word_count} words in the novel {novel}")
    for dict in dict_list:
        if dict["name"].isalpha():
            print(f"The {dict["name"]} character was found {dict["num"]} times")
    print("------End report------")

main()
