def find_repeated_items(tuple1):

  item_set = set(tuple1)

  repeated_items = []
  for item in item_set:
    if tuple1.count(item) > 1:
      repeated_items.append(item)

  return repeated_items

tuple1 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
repeated_items = find_repeated_items(tuple1)
print(repeated_items)