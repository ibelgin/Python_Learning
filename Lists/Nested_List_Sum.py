def nested_sum(lst):
  total = 0
  for i in lst:
    total+=sum(i)
  print(total)

nested_sum([ [1, 2], [3], [4, 5, 6] ])
