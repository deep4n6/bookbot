def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(text):
    formatted_text = text.lower()
    my_dict ={}
    for char in formatted_text:
        if char in my_dict:
            my_dict[char] += 1
        else: 
            my_dict[char] = 1
    return my_dict

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_dict):
    # Create an empty list to store our dictionaries
    chars_list = []
    
    # Convert each character and count to a dictionary and add to list
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list based on count (using your sort_on function)
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

