def shortestPalindrome(s):
    if not s:
        return ""

    # Function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    for i in range(len(s), 0, -1):
        # Check if the substring s[:i] is a palindrome
        if is_palindrome(s[:i]):
            # Reverse the remaining part of the string and append it to the beginning
            return s[i:][::-1] + s

    return ""  # Return an empty string if no palindrome found

# Test cases
s1 = "aacecaaa"
print(shortestPalindrome(s1))  # Output: "aaacecaaa"

s2 = "abcd"
print(shortestPalindrome(s2))  # Output: "dcbabcd"

'''
Algorithm
1 Define a function shortestPalindrome(s) that takes a string s as input.
Inside the function:
  a Check if the input string s is empty. If it is, return an empty string.
  b Define a helper function is_palindrome(string) that checks if a given string is a palindrome by comparing it with its reversed version.
  c Iterate from the end of the string towards the beginning using a for loop.
  d For each iteration:
     a Check if the substring from index 0 to the current index i is a palindrome using the is_palindrome helper function.
     b If a palindrome is found:
        a Extract the remaining part of the string after the palindrome (from index i to the end of the string).
        b Reverse the remaining part of the string and append it to the beginning of the original string s.
        c Return the newly constructed shortest palindrome.
  e If no palindrome is found, return an empty string (indicating that the input string itself is empty or there are no palindromes).
3 Return the shortest palindrome formed by adding characters to the beginning of the original string s.
'''