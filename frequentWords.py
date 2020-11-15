from collections import Counter #supports convenient and rapid tallies
import re
def top_3_words(text):
    counts = Counter(re.findall("'?[a-z][a-z']*", text.lower())) #an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values
    return [w for w, words in counts.most_common(3)]
  

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))