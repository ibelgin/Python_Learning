def is_sorted(lst):
  temp = list(lst)
  temp.sort()
  print(temp)
  if (lst == temp):
    print("Sorted")
  else:
    print("Not Sorted")

is_sorted([1, 5,2])
