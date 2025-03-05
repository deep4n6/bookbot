# Import functions from stats.py
from stats import get_num_words, char_count, chars_dict_to_sorted_list
import sys

def main():
    

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Path to the book
    path = sys.argv[1]
    
    # Read the book file
    with open(path) as f:
        file_contents = f.read()
    
    # Get word count
    word_count = get_num_words(file_contents)
    
    # Get character count dictionary
    chars_dict = char_count(file_contents)
    
    # Convert to sorted list
    chars_list = chars_dict_to_sorted_list(chars_dict)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count (alphabetical only)
    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Call the main function
if __name__ == "__main__":
    main()