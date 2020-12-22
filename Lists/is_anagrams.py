def is_anagrams(str1,str2):
  if (sorted(str1) == sorted(str2)):
    print("Yes")
  else:
    print("No")

is_anagrams( "rac", "car")
