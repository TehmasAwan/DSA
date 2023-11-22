from collections import defaultdict

def are_anagrams(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_freq = defaultdict(int)

    
    for char in str1:
        char_freq[char] += 1

    
    for char in str2:
        if char_freq[char] == 0:
            return False  
        char_freq[char] -= 1

    return True  

string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
if result:
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
