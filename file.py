
myFile = open('myfile.txt', 'w')


print('name', myFile.name)

print('is Closed', myFile.closed)

print('opening mode', myFile.mode)


myFile.write('I love code in Python Because easy to understand and very fast.')

myFile.write('and one more think is its easy to use.')

myFile.close()

myFile = open('myFile.txt', 'a')

myFile.write(' I also like php and Javascript.')

myFile.close()

myFile = open('myFile.txt' , 'r+')

text = myFile.read(100)

# print(text)

second = open('main.py', 'w')
second.close()
third = open('index.html','w')

print(second.name)

third.write('<button>Click</button>')

third.close()

third = open('index.html', 'a')
third.write('<p>hello world</p>')

third.close()

third = open('index.html','r+')
read = third.read(100)
print(read)