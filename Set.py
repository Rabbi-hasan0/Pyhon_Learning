thisset = {"apple", "banana", "cherry", "apple"}
#print
print(thisset)
#print type of set
print(type(thisset))
#print using for each loop
for x in thisset:
  print(x)
#print if in set
print("banana" in thisset)
print("banana" not in thisset)
#Add element
thisset.add("orange")

#Update in set
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# #update set with list
my = ["kiwi", "orange"]
thisset.update(my)

#remove in set
thisset.remove("banana")
thisset.discard("apple")
print(thisset)
x = thisset.pop()
print(x)
thisset.clear()
print(thisset)
