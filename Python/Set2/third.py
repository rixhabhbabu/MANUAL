def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()  # Split text into words using whitespace
            return len(words)
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Get input from user
file_path = input("Enter the path to the text file: ")

# Count words and display result
word_count = count_words(file_path) 
print(f"Number of words in the file: {word_count}")