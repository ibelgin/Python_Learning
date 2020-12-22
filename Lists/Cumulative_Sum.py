def cum_sum(lst):
  temp = 0
  final_list=[]
  for i in lst:
    temp=temp+i
    final_list.append(temp)
  print(final_list)

cum_sum([1,2,3])
# Output - [1,3,6]
