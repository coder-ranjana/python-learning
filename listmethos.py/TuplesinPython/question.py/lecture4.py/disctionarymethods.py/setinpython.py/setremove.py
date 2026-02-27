collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("Ranjana Rauniyar")
collection.add((1, 2, 3))


collection.remove("Ranjana Rauniyar")#this will raise an error becouse the element is not persent in the set)
print(len(collection))
