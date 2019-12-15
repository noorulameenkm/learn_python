integer = 12
floating = 12.0
array = [1,2,3,4,5]


print('Location of integer now is ', id(integer))
print('Location of floating now is ', id(floating))
print('Location of array now is ', id(array))

"""
    Changing the values below, and checking the memory again
"""

integer = 13
floating = 13.0
array.append(6)


print('Location of integer after changing is ', id(integer))
print('Location of floating after changing is ', id(floating))
print('Location of array after changing is ', id(array))

