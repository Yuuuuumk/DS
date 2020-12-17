def vc_count(word):
    return v2(word, 0, 0, 0)

def v2(word, i, v, c):
    if i == len(word):
        return [v, c]
    else:
        if word[i] in "aeiouAEIOU":
            return v2(word, i + 1, v + 1, c)
        else:
            return v2(word, i + 1, v, c + 1)
    

print(vc_count('aeiuopjdhahd'))