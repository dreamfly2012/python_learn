sample = [1, ["another", "list"], ("a", "tuple")]

mylist = ["List item 1", 2, 3.14]

print(mylist[:])

print(mylist[0:2])

name = "Stavros"

print("Hello, {}!".format(name))

print(range(1,10))

list = list(range(1, 10))
print(list)

funcvar = lambda x: x + 1

y = funcvar(2)
print(y)


## classes ##
class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable
classinstance = MyClass()
info = classinstance.myfunction(2,4)
print(info)
classinstance.common = 10
print(classinstance.common)

## file operate ##
import pickle
mylist = ["this","is", 4,  1234]
myfile = open(r"data.dat","wb")
pickle.dump(mylist, myfile)
myfile.close()

myfile = open(r"data.dat", "rb")
loadedlist = pickle.load(myfile)
print(loadedlist)
myfile.close()

myfile1 = open("test.txt", "w")
myfile1.write("this is text file")
myfile1.close()

with open("test.txt") as fh:
    print(fh.read())

## chain operator ##
list1 = [1,3,5]
list2 = [2,4,6]

print([x * y for x in list1 for y in list2])

print(any([i % 3 for i in list1]))



