import re

def word_count(s):
    # Your code here
    cache = {}
    if len(s) == 0:
        return cache

    string = re.sub('[^a-zA-Z0-9 ]', '', s).lower()
    words_in_string = string.split(" ")
    
    for char in words_in_string:
            if char in cache:
                cache[char] += 1
            else: 
                cache[char] = 1
    
    return cache
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))