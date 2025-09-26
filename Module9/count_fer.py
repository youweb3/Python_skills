import string

def x (text):
    if not text:
        return{}
    
    text = ''.join(a for a in text if a not in string.punctuation).lower()
    words = text.split()#split the text into words

    frequency = {} #Initialize the word frequency

     # Recursive helper function to process the words
    def process_words(words, index):
         # Base case: all words processed
        if index == len(words):
            return
        
        # Get the current word
        word = words[index]

        # Update the word frequency dictionary
        if word in frequency:
            frequency[word] +=1
        else:
            frequency[word] =1
        
        # Recursive call to process the next word
        process_words(words, index + 1)

            # Call the recursive helper function
    process_words(words, 0)
    
    return frequency


# Test the word frequency counter
text = "This a Word_Frequency_Counter. It contains some words. inside a 'function' Some words are repeated, some not'."
frequency_dict = x (text)

# Print the word frequency dictionary
for word, count in frequency_dict.items():
    print(f"{word}: {count}")

