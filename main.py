#print("hello world")

text_path = "books/frankenstein.txt"

def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_word(text):
    new_list = text.split()
    return len(new_list)

def count_char(text):

    #my_string = "FOR FRODO"
    lowered_string = text.lower()
    
    count_char = {}
    for ch in lowered_string:
        if ch in count_char.keys():
            count_char[ch] += 1
        else:
            count_char[ch] = 1
    
    newSorted_lst = change_dict_listDict(count_char)
    
    return newSorted_lst
    
def change_dict_listDict(dict):
    lst = []
    def sort_on(dict):
        return dict["num"]
    
    for k in dict.keys():
        temp_dict = {}
        if k.isalpha():
            temp_dict["char"] = k
            temp_dict["num"] = dict[k]
            lst.append(temp_dict)
    
    
    #print(lst)
    lst.sort(reverse=True, key=sort_on)
    return lst



def main():
    full_text = read_file(text_path)
    print(f"--- Begin report of {text_path} ---")
    print(f"{count_word(full_text)} words found in the document")
    print(" ")

    count_char_lst = count_char(full_text)
    for item in count_char_lst:
        char = item["char"]
        num = item["num"]
        print(f"The {char} character was found {num} times")
    
    print(f"--- End report ---")



main()