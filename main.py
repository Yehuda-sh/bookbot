with open("books/frankenstein.txt") as f:
    book_contents = f.read()
# print(book_contents)

def count_words(book_contents):
        
    
    count_of_words = 0
    count_characters = {}




    for word in book_contents:

            if isinstance(word, str):
                count_of_words += 1
                for char in word.lower():
                    if char in count_characters:
                        count_characters[char] += 1
                   
                    else :
                        count_characters[char] = 1
    return count_of_words ,count_characters        
    
      
def print_report(count_of_words ,count_characters):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_of_words} words found in the document')

    sorted_characters = sorted(count_characters.items(), key=lambda x: x[1], reverse=True)

    for char ,count in sorted_characters:
        if char.isalpha():
            print(f"The character \'{char}\' was found {count} times")

    
    print('--- End report ---')


count_of_words, count_characters = count_words(book_contents)
print_report(count_of_words, count_characters)

