import re
def top_3_words(text):
  if len(text) <= 0:
    return []
  
  checked = {} #words and the frequency they appear in the text
  regex = re.compile('[,/\.!?]')
  invalid = """ '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
  for word in text.lower().split():
    if word not in checked:
      word = regex.sub('', word)
      if word not in invalid:
        checked[word] = text.count(word)

  print(checked["i"])
  return sorted(checked, key=checked.get, reverse = True)[:3] 
  

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
