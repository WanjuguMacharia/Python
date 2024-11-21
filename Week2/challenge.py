# books = ('crossings', 'little sins', 'inferno', 'harry porter', 'frankinstein')

# for x in books:
#     print(x)

myDict = {}

keys = ['name', 'age', 'favorite color']

for key in keys:
    value = input(f'What is your {key}:')

    myDict[key] = value

    print('/nCollected info:')
    print(myDict)