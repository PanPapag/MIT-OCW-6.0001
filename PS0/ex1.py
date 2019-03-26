import math

expression = '6 + 4 * 10 = '+ repr(6 + 4*10)
print(expression)

expression = '(6 + 4) *10 = '+ repr((6 + 4)*10)
print(expression)

expression = '23^5 = '+ repr(23**5)
print(expression)

x = (-68 + math.sqrt(68*68 - 4*10*68))/(2*10)
expression = 'Positive root of 10*x^2 + 68*x - 510 : '+ repr(x)
print(expression)

expression = 'cos(3.4)^2 + sin(3.4)^2 = '+ repr(math.cos(3.4)**2+math.sin(3.4)**2)
print(expression)
