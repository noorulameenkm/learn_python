arr = [1,2,3,4,5,6,7,8,9,10]

odd = list(filter(lambda n: n % 2 != 0, arr))
even = list(filter(lambda n: n % 2 == 0, arr))

print('Odd numbers are ', odd)
print('Even numbers are ', even)