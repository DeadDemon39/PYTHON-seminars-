# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# Input: 5
# Output: 120


n = int(input("Введите неотрицательное число: "))

if n < 0:
    print("Ввели отрицательное число! Введите пожалуйста положительное число:")

count = 1
factorial = 1

while count <= n:
    factorial = factorial * count
    count = count + 1
print(f"Факториал числа {n} = {factorial}")


# factorial = 1
# while n:
#     factorial *= n
#     n -= 1
# print(factorial)




