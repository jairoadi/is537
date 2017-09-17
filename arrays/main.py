from array_api import Array
import csv

with open("/Users/jairof/Documents/is537/arrays/data_example.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    array = None
    linenum = 0
    for row in reader:
        print(str(linenum)+":"+str(row[0])+","+str(row[1])+","+str(row[2]))
        if str(row[0]) == 'CREATE':
            array = Array();'creating an object array'
        elif  str(row[0]) == 'ADD':
            array.add(str(row[1]))
        elif  str(row[0]) == 'DEBUG':
            array.debug_print()
        elif  str(row[0]) == 'SET':
            array.set(int(row[1]),str(row[2]))
        elif  str(row[0]) == 'GET':
            array.get(int(row[1]))
        elif  str(row[0]) == 'DELETE':
            array.delete(int(row[1]))
        elif str(row[0]) == 'INSERT':
            array.insert(int(row[1]),str(row[2]))
        elif str(row[0]) == 'SWAP':
            array.swap(int(row[1]), str(row[2]))

        linenum += 1

# objectArray = Array(); 'creating an object array'
#
# 'here I will do all the work'
#
# print(0, ':CREATE,')
# objectArray.debug_print()
# objectArray.add('a')
# objectArray.add('e')
# objectArray.add('r')
# objectArray.add('o')
# objectArray.add('l')
# objectArray.add('o')
# objectArray.add('d')
# objectArray.add('u')
# objectArray.add('s')
# objectArray.add('a')
# objectArray.debug_print()
# objectArray.add('u')
# objectArray.debug_print()
# objectArray.set(4,'S')
# objectArray.set(12,'M')
# objectArray.debug_print()
# objectArray.get(8)
# objectArray.get(11)
# objectArray.insert(21, 'b')
# objectArray.insert(4, 'i')
# objectArray.insert(4, 'L')
# objectArray.insert(4, 'w')
# objectArray.insert(4, 'x')
# objectArray.insert(4, 'T')
# objectArray.insert(4, 'y')
# objectArray.debug_print()
# objectArray.delete(6)
# objectArray.debug_print()
# objectArray.delete(10)
# objectArray.debug_print()
# objectArray.delete(11)
# objectArray.debug_print()
# objectArray.delete(7)
# objectArray.debug_print()
# objectArray.delete(13)
# objectArray.debug_print()
# objectArray.swap(1,3)
# objectArray.swap(7,8)
# objectArray.debug_print()
# objectArray.swap(0,13)
# objectArray.delete(10)
# objectArray.debug_print()
# objectArray.add('u')
# objectArray.add('h')
# objectArray.debug_print()
# objectArray.insert(12, 'p')
# objectArray.add('T')
# objectArray.add('g')
# objectArray.add('h')
# objectArray.add('t')
# objectArray.debug_print()
# objectArray.insert(25, 'y')
# objectArray.set(15,'o')
# objectArray.insert(27, 'G')
# objectArray.debug_print()
# objectArray.set(10,'D')
# objectArray.swap(16,13)
# objectArray.debug_print()
# objectArray.insert(8, 'F')
# objectArray.insert(7, 'o')
# objectArray.insert(13, 't')
# objectArray.set(14, 'e')
# objectArray.swap(0,9)
# objectArray.swap(3,13)
# objectArray.debug_print()