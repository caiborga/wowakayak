def is_palindrome(string):
    reverse = string [::-1]
    if reverse == string:
        return True
    return False

def remove(array):
    result = []
    for i in range(0,len(array)-1):
        if len(array[i]) > 1:
            result.append(array[i])
    return result

def palindromes(palindrome_string) -> list:

    CutStart = palindrome_string
    CutEnd = palindrome_string [:-1]
    palindrome = []
       
    if is_palindrome(palindrome_string):
        palindrome.append(palindrome_string)
        return palindrome

        #while 1 and 2 browse palindrome_string for palindromes and saves them in list palindrome
        #while loop 2 is looking in CutEnd for palindromes (part of palindrome_string reduced by last char of palindrome_string)
        #and cuts them out of CutStart (at least a single char, so while loop 1 can stop). 
        #After that CutEnd is refilled with the remaining part of palindrome_string (saved in CutStart) and this way 
        #crawls the whole palindrome_string step by step

    while len(CutStart)!=0: #1
        while len(CutEnd)!=0: #2 
            if is_palindrome(CutEnd):
                palindrome.append(CutEnd)
                CutStart = CutStart [len(CutEnd):]
                CutStart = CutStart [::-1]
                CutEnd = CutEnd [len(CutEnd):]
            CutEnd = CutEnd [:-1]
        CutEnd = CutStart
    palindrome = remove(palindrome)
    return palindrome
