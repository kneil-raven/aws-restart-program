# Exercise 1
# define a list
# myFruitList = ["apple", "banana", "cherry"]
# print(myFruitList)
# print(type(myFruitList))

# # access list by position
# print(myFruitList[0])
# print(myFruitList[1])
# print(myFruitList[2])

# # changing the values in a list
# myFruitList[2] = 'orange'
# print(myFruitList)



# Exercise 2
# tuple data type
# myFinalAnswerTuple = ("apple", "banana", "pineapple")
# print(myFinalAnswerTuple)
# print(type(myFinalAnswerTuple))

# # acceessing tuple by position
# print(myFinalAnswerTuple[0])
# print(myFinalAnswerTuple[1])
# print(myFinalAnswerTuple[2])


# Exercise 3
# dictionary data type
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)


# accessing dictionary by name
# print(myFavoriteFruitDictionary['Akua'])
# print(myFavoriteFruitDictionary['Saanvi'])
# print(myFavoriteFruitDictionary['Paulo'])


# testing
# changing value in Akua
myFavoriteFruitDictionary['Akua'] = 'bear brand' 
print(myFavoriteFruitDictionary)

# # changing key-name
# myFavoriteFruitDictionary['Fruitas'] = myFavoriteFruitDictionary.pop('Akua')
# print(myFavoriteFruitDictionary)

# # convert from dictionary to tuple
# tupleFruitDictionary = myFavoriteFruitDictionary.items()
# print(tupleFruitDictionary)
# # #converting back to dictionary
# sortedTuple = dict(sorted(tupleFruitDictionary))
# print(sortedTuple)


# test by sir Justin
# step 1: sort the keys
test = {}

# Step 1: Sort the keys first
mySortedFruits = sorted(myFavoriteFruitDictionary.keys())
#print(mySortedFruits)


# Step 2: Print values by key
for key in mySortedFruits:
    test[key] = myFavoriteFruitDictionary[key]
    print(key, myFavoriteFruitDictionary[key])
