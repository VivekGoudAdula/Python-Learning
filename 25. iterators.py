# ITERATORS
# Iterator is an object which has countable number of values, which can be iterated upon, like we can traverse through all values
# Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

# ITERATOR vs ITERABLE 
# Lists, Tuples, Dictionaries and Sets are iterable objects by using which you can get an iterator from
# All these objects have an iter() method which is used to get an iterator

# LIST
mylist = [5,4,3,2]
iteration = iter(mylist)
print(next(iteration))
print(next(iteration))

# STRING

a = "Alexa"
it = iter(a)
print(next(it))
print(next(it))

# ---------------------------------------------------------

# LOOPING THROUGH AN ITERATOR

for i in mylist:
    print(i)

# ---------------------------------------------------------

# CREATE YOUR OWN ITERATOR
class numbers:
    def __iter__ (self):
        self.num = 1
        return self
    def __next__(self):
        x = self.num
        self.num+=1
        return x
n1 = numbers()
myiter = iter(n1)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# ---------------------------------------------------------

# STOPITERATION EXCEPTION

class nums:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration
num = nums()
iteration = iter(num)
for number in iteration:
    print(number)

# ---------------------------------------------------------