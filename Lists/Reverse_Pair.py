# Two words are a “reverse pair” if each is the reverse of the other. Write a
# program that finds all the reverse pairs in the word list.

# Eg: [ rat, mat, tar, tap, pat]
# Here there are two pairs
# rat - tar
# tap - pat

def reverse_pair(lis_main):
  lst = list(lis_main)
  for i in lst:
    if (i[::-1] in lst):
      print(i ,"-",i[::-1])
      lst.remove(i)
    else:
      continue

reverse_pair([ 'rat', 'mat', 'tar', 'tap', 'pat'])
