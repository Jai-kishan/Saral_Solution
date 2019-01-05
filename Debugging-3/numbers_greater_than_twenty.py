#pass by reference and function
def numbers_greater_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
    	list.remove(item)
    else:
    	counter+=1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_20 = numbers_greater_than_twenty(num_list)
print(num_list)