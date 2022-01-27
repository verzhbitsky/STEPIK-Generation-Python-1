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


# a = int(input())
# b = int(input())
# counter = 0
# largest = 0
# for i in range(a, b + 1):
#     total = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             total += j
#         if total >= counter and i >= largest:
#             counter = total
#             largest = i
# print(largest, counter)

# a = int(input())
# s = 0
# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             s += 1
#     print(i, s*'+', sep='')
#     s=0

# num = int(input())
# while num > 9:
#     sum = 0
#     while num > 0:
#         last_digit = num % 10
#         sum += last_digit
#         num //= 10
#     num = sum
# print(num)


# n = 5
# fac = 1
# for i in range(1, n + 1):
#     fac *= i
# print(fac)


# n = 20
# fac = 1
# sum_fac = 1
# for i in range(1, n):
#     fac *= i
#     for j in range(i + 1):
#         sum_fac += fac
# print(sum_fac)

# a = int(input())
# b = int(input())
# sm = 0
# for x in range(a, b + 1):
#     count = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             count += 1
#     if count == 2:
#         print(x)


# a = 15
# counter = 0
# for i in range(2, a + 1):
#     if i % 1 == 0 and i % i == 0:
#         for j in range(1, i + 1):
#             print(j)



# city1 = str(input())
# city2 = str(input())
# city3 = str(input())
#
# if len(city1) <= len(city3) <= len(city2):
#     print(city1)
#     print(city2)
# elif len(city3) <= len(city1) <= len(city2):
#     print(city3)
#     print(city2)
# elif len(city3) <= len(city1) <= len(city2):
#     print(city3)
#     print(city2)
# else:
#     print(city1)
#     print(city3)

# email = input()
# c = "@"
# d = "."
# counter = 0
# if c in email:
#     counter += 1
# if d in email:
#     counter += 1
#
# if counter == 2:
#     print("YES")
# else:
#     print("NO")


# n = 8
# count = 0
# maximum = -10 ** 6 - 1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x >= maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# n = 4
# count = 0
# maximum = -10 ** 4 - 1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x >= maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# n = int(input())
# for i in range(1):
#     print('*' * 19)
#     for j in range (n - 2):
#         print('*', ' ' * 15, '*')
#     print('*' * 19)

# n = int(input())
# num = 0
# for i in range(n):
#     num = n % 10
#     if i == 1:
#         break
#     n //= 10
# print(num)

# num = int(input())
# rew_num = ''
# count = 0
# count1 = 0
# n1 = 0
# a = 0
# while num > 0:
#     count = num % 10
#     rew_num = rew_num + str(count)
#     num //= 10
# n_num = int(rew_num)
# while n_num > 0:
#     n1 = n_num % 10
#     count1 += 1
#     n_num //= 10
#     if count1 == 3:
#         a = n1
# print(a)


# num = int(input())
# last_number = num % 10
# n = 0
# count_3 = 0
# count_last = 0
# count_even = 0
# sum_5 = 0
# sum_7 = 1
# sum_0_5 = 0
# while num > 0:
#     n = num % 10
#     if n == 3:
#         count_3 += 1
#     if n == last_number:
#         count_last += 1
#     if n % 2 == 0:
#         count_even += 1
#     if n > 5:
#         sum_5 += n
#     if n > 7:
#         sum_7 *= n
#     if n == 0 or n == 5:
#         sum_0_5 += 1
#     num //= 10
# print(count_3)
# print(count_last)
# print(count_even)
# print(sum_5)
# print(sum_7)
# print(sum_0_5)

# n = int (input('Введите ограничение диапазона для\
# \nнахождения чисел Рамануджана  :)'))
# total = 0
# for n in range(1, n):
#     for k in range(1, n):
#         for m in range(1, n):
#           for t in range(1, n):
#               if n**3 + k**3 == m**3 + t**3 and n!=t and k!=m and k!=t  and  n>k and m>t and n>m:
#                 n,k ==m, t
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m, 't=',  t, '=',n **3 + k **3 )
# print('Общее количество натуральных решений =', total)
#


# str1 = input()
# for i in range(-1, -len(str1) - 1, -1):
#     print(str1[i])

# first_name = input()
# last_name = input()
# otch = input()
#
# print(last_name[0], first_name[0], otch[0], sep="")


# s = input()
# s_num = '0123456789'
# counter = 0
# for i in range(len(s)):
#     for j in range(len(s_num)):
#         if s[i] == s_num[j]:
#             counter += 1
# if counter > 0:
#     print("Цифра")
# else:
#     print("Цифр нет")








