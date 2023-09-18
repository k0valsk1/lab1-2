#Task1
print(4, 8, 15, 16, 23, 42)
#task2
print(4, 8, 15, 16, 23, 42, sep='\n')
#task3
a = int(input())
print(a, a+1, a+2, sep='\n')
#task4
a = int(input())
b = int(input())
c = int(input())
print(a+b+c)
#task5
a = int(input())
print('Volume =' , a*a*a)
print('Total surface area =', 6*a*a)
#task6
a = int(input())
b = int(input())
print(b//a)
print(b%a)
#task7
a = int(input())
print('The digit in the thousands position is', a//1000)
print('The number in the hundreds position is', a//100%10)
print('The digit in the tens position is', a//10%10)
print('The digit in the position of units is', a%10)
#task8
 a=int(input())
b=a/2
print(round(b))

#task9
a=int(input())
result = a << 1
if(result) == 0:
   print('WARNING')
else:
   print('The result of << is', a)

#task10
a=int(input('Please enter the first number:'))
b=int(input('Please enter the second number:'))
c=input('Please choose the operation (+, -, *, /):')

if(c=='+'):
   print(a+b)

elif(c=='-'):
   print(a-b)

elif(c=='*'):
   print(a*b)

elif(c=='/'):
   print(a/b)