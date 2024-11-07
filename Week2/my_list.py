## create an empty list
my_list = []

##append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)


## Insert value
my_list.insert(2, 15)

print(my_list)

## Extend list
my_list.extend([50, 60, 70])

print(my_list)

## Remove last element from list
my_list.pop(-1)

print(my_list)

## Sort in ascending order
print(sorted(my_list))

## Print index of value
numCount = my_list.index(30)

print(numCount)
