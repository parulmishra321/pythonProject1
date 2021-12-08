#Concatenate two lists index-wise i.e. input lists = ['te','inp'] and ['st','ut'] output list = ['test', 'input']

def concatenate_lists(l1, l2):
   return [i + j
      for i, j in zip(l1, l2)
   ]

l1 = ['te','inp']
l2 = ['st','ut']

print("Input lists:")
print(l1)
print(l2)
print("\nOutput list:")
print(concatenate_lists(l1, l2))