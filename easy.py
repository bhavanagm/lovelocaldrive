def length_of_last_word(s):
    # Split the string into words by spaces and filter out empty strings
    words = s.split()
    
    # Return the length of the last word
    return len(words[-1])

# Test cases
s1 = "Hello World"
print(length_of_last_word(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print(length_of_last_word(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(length_of_last_word(s3))  # output:5

'''
Algorithm
1 Define a function length_of_last_word(s) that takes a string s as input.
2 Split the input string into words using the split() method, which separates the string into a list of words based on spaces. Store this list in a variable words.
3 Retrieve the last word from the list of words. To do this:
4 Access the last element of the list words using words[-1], which represents the last word in the string after splitting.
5 Calculate the length of the last word using the len() function. This gives the length of the last word in the input string.
6 Return the length obtained in the previous step as the output of the function.'''