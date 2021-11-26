def rotate_word(word, n):
  new_s = ''
  for c in word:
    if c.isupper():
      one = ord('A')
    elif c.islower():
      one = ord('a')
    
    rotn = ord(c) + n
    if rotn < one:
      rotn += 26
    new_s += chr(rotn)
       
  return new_s

rotate_word('melon', -10)
