lst1 = [1, 2, 4, 6, 7, 5 ]

lst2 = lst1 + [1]

 
print(lst1)
print(lst2)
print("_"*20)

lst2 = lst1
lst2 += [1] 

print(lst1)
print(lst2)

for i in lst2:
  print(i)

for i in range(len(lst2)):
  lst2[i] += 5
  print(lst2[i])

print( lst2)

for i in "text":
  print(i)



