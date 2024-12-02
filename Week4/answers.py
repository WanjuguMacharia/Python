import os

file = open("myFile.txt", "w")
file.write('It is a beautiful day')
file.close()

file = open('myFile.txt', 'a')
file.write(' Python is awesome')

file = open('myFile.txt', 'r')
data = file.read()

print(data)


try:
    file = open('myFile.txt', 'r')
    print(file.data())
except AttributeError:
    print('Error')


os.remove('anotherFile.txt')
