
'''This is the reverse string exercise'''

# name = 'Sarah has a pretty face'
# tempName = []
# newName = []
# iCount = 1
#
#
# tempName = name.split(' ')
#
# while iCount <= len(tempName):
#     newName.append(tempName[len(tempName) - iCount])
#
#     iCount += 1
#
# print('old name: ' + name)
# name =' '.join(newName)
# print('new name: ' + name)


'''Write a program to print out the first n primes'''

i = 0

while i <= 100:

    if i == 2:
        print(i, ' is PRIME')
    elif i % 2 == 0:
        print(i , ' is not prime')
    else:
        print(i, ' is PRIME')

    i +=1


'''You have an array of red balls and blue balls.Sort them in linear time and constant space so that all the red balls
 are in the front, and all the blue balls in the back'''

# bagArray = ['red','blue','red','red','blue','blue']
#
#
#
#
# '''remove duplicates from an array'''
#
# '''Write down prime numbers unto 20. Write the most efficient code that you know of.'''
#
#
# foo = [1,2,[3,[4,5],6]]
# #
# # print(foo)
#
# for i, value in enumerate(foo):
#     if(isinstance( value, int )):
#         if(isinstance( value, [] )):
#             for i, value2 in enumerate(value):
#                 print(value2)
#         print(value)