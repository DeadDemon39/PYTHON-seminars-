# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Input: 5 
# Output: 6

A = int(input("Введите положительно число > 1: "))
count = 3
fibonachi = -1
c = 1
d = 1

while fibonachi < A:
    fibonachi = c + d
    c = d
    d = fibonachi
    count += 1
    print(fibonachi)

if fibonachi == A:
    print(count)
else:
    print(-1)


