def square(a):
    print(a)
    a = a**2
    return a
    
def func(a):
    a = 2 * a
    print(a)
    return square(a)
a = 2
print(a)
b = func(a)
print(a)

count = 0

def greet(a):
    if a%2 == 1:
        print("Hello")
    a = 5
    return a
    
def hello(a):
    for i in range(10000):
        if i%2 == 0:
            print("Hello")
        else:
            greet(i)
       
#hello(10)

string = ''
with open('ProgressTest/Names.txt', 'r') as file:
    for name in file.readlines():
        string += name.rstrip()

print(string)
print('416th letter: ', string[415])