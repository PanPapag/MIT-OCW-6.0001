import math

#give input
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
#do the calculations and print the result
power = x**y
s1 = repr(x) + '^' + repr(y) + ' = ' + repr(power)
print(s1)

log = math.log(x,2)
s2 = 'log(' + repr(x) + ') = ' + repr(log)
print(s2)
