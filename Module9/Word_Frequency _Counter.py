import string

def frequency_counter (text): #main function
    #Counts the frequency of each word in the input text.
    #:param text: string
    #:return: dictionary with word frequency

    #Base case: empty input
    if not text:
     return {}
    
    text = text.lower()
    text= ''.join(char for char in text if char not in string.punctuation)#Remove all punctuation from the text
    words =text.split() #split the text into words

    #Initialize the word frequency dictionary
    freq_dict = {}
    return word_recursive(words, freq_dict)


# Recursive helper function to update frequency dictionary
def word_recursive(words, freq_dict):
       

       #Base case: all words processed
       if not words:
           return freq_dict
       
       #get the current word
       word = words[0]

       #update the word frequency dictionary
       if word in freq_dict:
          freq_dict[word] += 1
       else:
          freq_dict[word] = 1

       #Recursive call for the remaining words
       return word_recursive(words[1:], freq_dict)


#test
text = "Python is fun! Python is easy."
result = frequency_counter(text)

for word, count in result.items():
    print(f"{word}: {count}")
