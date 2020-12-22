def has_duplicates(lst):
  temp_dict=[]
  for i in lst:
    if i not in temp_dict:
      temp_dict.append(i)
    else:
      return True
      break
  return False
      
print(has_duplicates([1,7,7,73,2,3]))
