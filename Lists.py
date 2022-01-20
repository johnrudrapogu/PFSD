Student  = [556, "Mothii", 84, 96, 84, 75, 84]
# print(Student)
# print(Student[0])
# print(Student[0 : 2])
# print(Student[2 : ])
# print(Student[ : 3])
# print(Student[ : ])
# print(Student[-1])
# print(Student[-1 : -7 : -1])
# print(Student[ : : -2])
# print(Student[1 : 7 : 2])
# print(Student[1 : 7 : 3])

## lists are mutbale

# for i in range(10, 1, -2):
#     print(i)

# L = [i for i in range(10)]
# print(L)

# a = [4, 7, 6, 8, 9]
# print(a)
#
# a [2] = 45
# print(a)
#
# a [2 : 5] = 10, 11, 12
# print(a)

# a = [4, 7, 6, 8, 9]
# b = [1, 2, 3]
# print(a + b)
#
# c = a + b
# print(c)
# print(a)
# print(b)
# print(a * 2)
# x = 7
# print(x in a)
# y = 10
# print(y in a)

## ALiasing
x = [10, 20, 30, 40, 50, 60]
y = x
# print(x)
# print(y)
# y [1] = 90
# y = x
# print()
# print(y)
# print(x)

# x.append([1, 3, 4])
# print(x)
#
# x.extend(2, 4, 5)
# print(x)

## Arrays in Python using lists
# a = [[1, 2], [3, 4], [5, 6]]
# print(a[1])
# print(a[2][1])
# for i in a[2]:
#     print(i)

## Tuples - immutable object - cant be modified or retrived on command. Elements of tuples can be called on
# tup = (10, 556, 22.3, "Mothi")
# print(tup)
# print(type(tup))

## Tuple within a Tuple
# Students = ("RAVI", "CSE", 92.00), ("Ramu", "ECE", 93.00),


## Sets - is mutable and unordered. Can't order values through index but can be appended
# s = set("Applee")
# print(s)
#
# j = {4, 5, 6, 23, 6, 1, 4, 4, 9, 4, 6, 1}
# print(j)

## Dictionaries (Map in Java)
d = {'Regd.No' : 556, 'Name' : 'Mothi', 'Branch' : 'CSE'}
# print(d['Regd.No'])
# print(d['Name'])
# print(d['Branch'])

# print(d)
# d['Gender'] = 'Male'
# print(d)
# d['Branch'] = 'EEE'
# print(d)
# print(d.items())
# print(d.keys())
# print(d.items())
# print(d.values()) ## a value could also be a list
#
# for key in d.keys():
#     print(d.get(key))

# L = [i for i in range(10)]
# print(L)
# d = {'a' : {'c' : 123, 'd' : [1, 2, 3, 4]}, 'b' : [5, 6, 7, 8]}
# print(d['a'] ['d'])

## Functions
def add(x , y):
    return x + y

print(add(5,6))