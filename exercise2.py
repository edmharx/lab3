list1 = ["Food","Car","Movie","Book"]
list2 = ["Adobo", "Subaru", "Transformers", "Sherlock Holmes"]

listOfTuple = [(list1[x], list2[x])for x in range(len(list1))]

print (listOfTuple)