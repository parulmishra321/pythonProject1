#Slice list into 3 equals parts and reverse each part.

def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6]
list_chunked = (list(split(my_list, chunk_size)))
reversed_list = [elem[::-1] for elem in list_chunked]
print("Split List:")
print(list_chunked)
print("\nReveresed Split chunks:")
print(reversed_list)


