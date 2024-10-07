def is_palindrome(s):
    clean = ''.join(c.lower()for c in s if c.isalnum())
    #anything you put inside the join function will have no spaces
    #and converting (c) anything in the string (s) to lowercase
    if  len(clean) <= 1:
        return True
    if clean[0] == clean[-1]: #if the first letter in the string is the same as the last letter in the string
        return is_palindrome(clean[1:-1])

    return False

print(is_palindrome("A man, A plan, A canal, Panama"))
print(is_palindrome("no 'X' in Nixon"))