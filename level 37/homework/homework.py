def obfuscate(email):
    return email.replace("@", " [at] ").replace("."," [dot] ")

def array(string):
    if len(string.split(",")) <= 2:
        return None
    return " ".join(string.split(",")[1:-1])

def temple_strings(obj, feature): 
    return obj + " are " + feature

def contamination(text, char):
    return len(text) * char

def is_palindrome(s):
    return s[::-1].lower() == s.lower()