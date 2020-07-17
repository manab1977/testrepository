listA = [1, 2, 3, 4]
listB = ['a', 'b', 'c', 'd']

zl = zip(listA, listB)

zl = list(zl)
print ("Before Zip")
print(listA)

print(listB)

print("After zip: " )
print(zl)

listC, listD = zip(*zl)
print("After Unzip:")

print(listC)

print(listD)


