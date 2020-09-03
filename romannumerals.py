def to_camel_case(text):
    text = list(text)
    for i in range(len(text)):
        if text[i-1] == "-" or text[i-1] == "_":
            text[i] = text[i].upper()
            text[i-1] = ""
            continue
        elif text[i].isupper():
            text[0] = text[0].upper()
            continue
    return "".join(text)