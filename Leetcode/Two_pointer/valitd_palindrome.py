s = "A man, a plan, a canal: Panamadd"



def is_palindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1

        while l < r and not s[r].isalnum():
            r -= 1

        
        if s[l].lower() != s[r].lower():
            return False 

        
        l += 1
        r -= 1

    
    return True


print(is_palindrome(s))