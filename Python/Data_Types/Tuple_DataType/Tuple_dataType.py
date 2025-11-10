# tuple data type in python(Properties of tuple is : 1. tuples are immutable , 2. duplicacy is allowed , 3. indexing based (index start with 0))

mytuple=(1,2,3,4,5,6,7,8,9,10) #this is a first way to create a tuple
print(type(mytuple))  #output : <class 'tuple'>
print(mytuple)       #output : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mytuple2=tuple() #this is a second way to create a tuple
print(type(mytuple2))  #output : <class 'tuple'>
mytuple3=tuple(1,2,3,4,5,6,7) #it will give  TypeError: tuple expected at most 1 argument, got 7
mytuple4=tuple([1,2,3,4,5,6]) #this is a third way to create a tuple from list
print(type(mytuple4))  #output : <class 'tuple'>
print(mytuple4)       #output : (1, 2, 3, 4, 5, 6)
mytuple5=() # this is a fourth way to create an empty tuple
print(type(mytuple5))  #output : <class 'tuple'>


# accessing tuple items using indexing and slicing

print(mytuple[0]) #output : 1
print(mytuple[1]) #output : 2
print(mytuple[2]) #output : 3
print(mytuple[3]) #output : 4
print(mytuple[4]) #output : 5
print(mytuple[5]) #output : 6
print(mytuple[6]) #output : 7
print(mytuple[7]) #output : 8
print(mytuple[8]) #output : 9
print(mytuple[9]) #output : 10
print(mytuple[-1]) #output : 10
print(mytuple[-2]) #output : 9
print(mytuple[-3]) #output : 8
print(mytuple[-4]) #output : 7
print(mytuple[-5]) #output : 6
print(mytuple[-6]) #output : 5
print(mytuple[-7]) #output : 4
print(mytuple[-8]) #output : 3
print(mytuple[-9]) #output : 2
print(mytuple[-10]) #output : 1
print(mytuple[2:7]) #output : (3, 4, 5, 6, 7)
print(mytuple[::2]) #output : (1, 3, 5, 7, 9)
print(mytuple[1::2]) #output : (2, 4, 6, 8, 10)
print(mytuple[::-1]) #output : (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(mytuple[::-2]) #output : (10, 8, 6, 4, 2)
print(mytuple[1::-2]) #output : (2)
print(mytuple[2::-2]) #output : (3, 1)
print(mytuple[-2::-2]) #output : (9, 7, 5, 3, 1)
print(mytuple[10::-2]) #output : (10, 8, 6, 4, 2)
print(mytuple[9::-2]) #output : (9, 7, 5, 3, 1)



# methods applicable on tuple data type

print(len(mytuple)) #output : 10
mytuple.append(11) #it will give AttributeError: 'tuple' object has no attribute 'append' because tuple is immutable
mytuple.insert(1,20) #it will give AttributeError: 'tuple' object has no attribute 'insert' because tuple is immutable
mytuple.extend([11,12,13]) #it will give AttributeError: 'tuple' object has no attribute 'extend' because tuple is immutable
mytuple.remove(5) #it will give AttributeError: 'tuple' object has no attribute 'remove' because tuple is immutable
mytuple.pop() #it will give AttributeError: 'tuple' object has no attribute
del mytuple[1] #it will give TypeError: 'tuple' object doesn't support item deletion because tuple is immutable
del mytuple  #it will delete the entire tuple
mytuple.clear() #it will give AttributeError: 'tuple' object has no attribute 'clear' because tuple is immutable
print(sum(mytuple)) #output : 55
print(min(mytuple)) #output : 1
print(max(mytuple)) #output : 10
print(mytuple.count(5)) #output : 1






# tuple data  structure is immutable, so we cannot change, add or remove items after the tuple is created.
# if we want to change our tuple, we have to convert it to a list, make the changes, and convert it back to a tuple.
mylist=list(mytuple) #convert tuple to list
print(type(mylist))  #output : <class 'list'>
print(mylist)       #output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist.append(11)    #add item to list
mytuple=tuple(mylist) #convert list back to tuple
print(type(mytuple))  #output : <class 'tuple'>
print(mytuple)       #output : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# -----we  can apply all list methods to change our tuple-----