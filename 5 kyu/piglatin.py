def pig_it(text):
    text = text.split()
    string = ""
    for words in text:
        if len(words) == 1:
            if words.isalpha():
                string += words + "ay" + " "
            else:
                string += words
            continue
        words = list(words)
        string += "".join(words[1:len(words)]) + words[0] + "ay" + " " 
    return string.strip()
