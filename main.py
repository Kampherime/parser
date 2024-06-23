
def get_wc(split_file):
    return len(split_file)

def split_file(file):
    file_contents = file.read()
    return file_contents.split(" ")

def main():
    with open("./books/frankenstein.txt") as f:
        word_list = split_file(f)
        word_count = get_wc(word_list)
        print(word_count)


main()
