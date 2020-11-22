import string
def rot13(message):
  alphabet = dict(zip(range(0,26), string.ascii_lowercase))
  message = list(message)
  for i in range(len(message)):
    if message[i].lower() in string.ascii_lowercase:
      if message[i].isupper():
        message[i] = alphabet[(ord(message[i].lower())-97+13)%26].upper()
      elif message[i].islower():
        message[i] = alphabet[(ord(message[i].lower())-97+13)%26]
  return "".join(message)
