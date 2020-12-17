"""
Assignment 1 question1 Anagram solutions
"""

def anagram(string1, string2):
    # Preprocess spaces
    string1 = string1.replace(" ","")
    string2 = string2.replace(" ","")

    # If length not equal, they are not anagram
    if (len(string1) != len(string2)):
        return False
        
    # Check letter by letter
    for i in range(len(string1)):
        next_character = string1[0]     # Grab the 1st char
        string1 = string1[1:]           # Reduce string1 by 1 char
        found_position = string2.find(next_character)   # look for this char in string2
        if (found_position != -1):  # modify string2 if found
            string2 = string2[0:found_position] + string2[found_position + 1:]
        #print(next_character)
    return len(string2) == 0
#def main():


