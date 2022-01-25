# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % 2 == 0:
#         flag = False
#         break
#
# if flag == True:
#     print("Simple number")
# else:
#     print("Combined number")

# result = 0
# for i in range(5):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break
#     num //= 10
# if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')

# num = int(input())
# devider = 2
# while True:
#     if num % devider == 0:
#         break
#     devider += 1
# print(devider)


# num = int(input())
# i = 0
# while num > i:
#     i += 1
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# count = 0
# p = 1
# for i in range(3):
#     x = int(input())
#     if x > 0:
#         p *= x
#         count += 1
#     elif x == 0:
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# count = 0
# p = 1
# for i in range(1, 4):
#     x = int(input())
#     if x > 0:
#         p = p * x
#         count = count + 1
#     elif x == 0:
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# mx = -10**6
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s = x + s
#     if mx < x < 0:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# s = 0
# for i in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s = s + n
# print(s)

# n = int(input())
# max_digit = 0
# counter = 0 #3?
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0 and digit != 0:
#         if digit > max_digit:
#             max_digit = digit
#     elif digit == 0:
#         counter += 1
#     n = n // 10
# if max_digit > 0:
#     print(max_digit)
# elif counter > 0:
#     print(0)
# else:
#     print("NO")


# n = int(input())
# while n > 0:
#     x = n
#     n //= 10
# print(x)

# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=" ")
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(5):
#         print(i + 1, end=" ")
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, "+", j, "=", i+j)
#     print()

# n = int(input())
# for i in range(n + 1):
#     for j in range(i):
#         print(i, end="")
#     print()


# for n in range(100):
#     for k in range(100):
#         for m in range(100):
#             if 10*n + 5*k + 0.5*m == 100 and n + k + m == 100:
#                 print(n, k, m)


# n = int(input())
# total = 0
# for i in range(n + 1):
#     for j in range(i):
#         total += 1
#         print(total, end=" ")
#     print()



# n = int(input())
# for i in range(n + 1):
#     for j in range(i):
#         print(j + 1, end="")
#     for j in range(i):
#         if j == 0:
#             continue
#         print(i-j, end="")
#     print()
#
