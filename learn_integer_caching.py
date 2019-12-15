"""
  integer from range -5 to 256 will refer to the same object,
  this is called integer caching
"""


a = 15
b = 15

print('Memory location of a now is ', id(a))
print('Memory location of b now is ', id(b))

a = 16
b = 16

print('Memory location of a after changing is ', id(a))
print('Memory location of b after changing is ', id(b))
