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


# s = input()
# counter_plus = 0
# counter_mult = 0
# for i in range(len(s)):
#     if s[i] == '+':
#         counter_plus += 1
#     if s[i] == '*':
#         counter_mult += 1
# print("Символ + встречается", counter_plus, "раз")
# print("Символ * встречается", counter_mult, "раз")

# s = input()
# counter = 0
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         counter += 1
# print(counter)


# s = input()
# s_low = s.lower()
# vocal_ch = "ауоыиэяюёе"
# unvocal_ch = "бвгджзйклмнпрстфхцчшщ"
# counter_voc = 0
# counter_unvoc = 0
# for i in range(len(s_low)):
#     for j in range(len(vocal_ch)):
#         if s_low[i] == vocal_ch[j]:
#             counter_voc += 1
#
#     for k in range(len(unvocal_ch)):
#         if s_low[i] == unvocal_ch[k]:
#             counter_unvoc += 1
#
#
# print("Количество гласных букв равно", counter_voc)
# print("Количество согласных букв равно", counter_unvoc)


# num = int(input())
# x = 0
# s = ''
# rev_s = ''
# for i in range(num):
#     x = num % 2
#     num //= 2
#     s += str(x)
#     if num == 0:
#         break
# for j in range(1, len(s) + 1):
#     rev_s += s[len(s) - j]
# print(rev_s)


# s = input()
# if s[:] == s[::-1]:
#     print("YES")
# else:
#     print("NO")


# общее количество символов в строке;
# исходную строку повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.

# s = input()
# print(len(s))
# print(s * 3)
# print(s[0:1])
# print(s[0:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:len(s) - 1])


# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.

# s = input()
# print(s[2:3])
# print(s[-2:-1])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-1::-2])


# s = input()
# if len(s) % 2 == 0:
#     half = len(s) // 2
#     s1 = s[:half]
#     s2 = s[(len(s)) // 2:]
# else:
#     half = (len(s) // 2) + 1
#     s1 = s[:half]
#     s2 = s[(len(s) + 1) // 2:]
# print(s2 + s1)


# name = input()
# if name.title() == name:
#     print("YES")
# else:
#     print("NO")

# s = input()
# counter = 0
# for c in s:
#     if c.islower() == True:
#         counter += 1
# print(counter)


# s = input()
# s = s.lower()
# print("Аденин:", s.count('а'))
# print("Гуанин:", s.count('г'))
# print("Цитозин:", s.count('ц'))
# print("Тимин:", s.count('т'))


# n = int(input())
# counter = 0
# for i in range(n):
#     s = input()
#     if '11' in s:
#         if s.count('11') > 2:
#             counter += 1
# print(counter)

# s = input()
# counter = 0
# for c in s:
#     if c.isnumeric():
#         counter += 1
# print(counter)

# s = input()
# if s.find('.com', len(s) - 4, len(s)) > 0:
#     print("YES")
# elif s.find('.ru', len(s) - 3, len(s)) > 0:
#     print("YES")
# else:
#     print("NO")

# s = input()
# counter = 0
# max_counter = 0
# max_char = s[0]
# counter = s.count(s[0])
# max_counter = counter
# for c in s:
#     if max_counter <= s.count(c):
#         max_counter = s.count(c)
#         max_char = c
# # print(max_counter)
# print(max_char)


# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') > 1:
#     print(s.find('f'), s.find('f', s.rfind('f')))
# else:
#     print("NO")


# s = input()
# first_in = s.find('h')
# last_in = s.rfind('h')
# print(s.replace(s[first_in:last_in + 1], ''))


# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# year = 2010
# price = '10k'
# currency = 'Bitcoin'
# print(s.format(year, price, currency))


# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# for i in range(26):
#     print(chr(ord('A') + i))


# a = int(input())
# b = int(input())
# s = ''
# for i in range(a, b + 1):
#     s += chr(i) + ' '
# print(s)


# s = input()
# new_s = ''
# for c in s:
#     new_s += str(ord(c)) + ' '
# print(new_s)


# print(chr(ord('D') - 3))

# num = int(input())
# s = input()
# new_s = ''
# x = 0
# for c in s:
#     if num > ord(c) - ord('a'):
#         x = ord(c) - ord('a')
#         new_s = new_s + chr((ord('z') - num) + (x + 1))
#     else:
#         new_s += chr(ord(c) - num)
# print(new_s)


# s = input()
# n = s.count('f')
# if n > 1:
#     print(s.find('f', s.find('f') + 1))
# elif n == 1:
#     print(-1)
# else:
#     print(-2)


# s = input()
# n_s = s[s.find('h') + 1:s.rfind('h')]
# rev_s = n_s[::-1]
# print(s.replace(n_s, rev_s))


# a = int(input())
# num = list(range(1, a + 1))
# print(num)


# num = int(input())
# chars = list()
# for i in range(97, 97 + num):
#     chars += chr(i)
# print(chars)


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[6] = 'Фиолетовый'
#
# print(rainbow)


# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])


# numbers1 = [1, 2, 3] * 2
# numbers2 = [6] * 9
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 + numbers2 + numbers3)


# s = list()
# for i in range(10):
#     s.append(i)
# print(s)


# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# Вывел список с удаленным первым и последним элементами.

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1,
#            11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1,
#            15, 1, 2, 14, 16, 6, 17, 5]
# counter = 0
# print(len(numbers))
# print(numbers[len(numbers) - 1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# del numbers[0]
# del numbers[len(numbers) - 1]
# print(numbers)

# n = int(input())
# languages = list()
#
# for i in range(n):
#     lang = input()
#     languages.append(lang)
# print(languages)

# abc = list()
# for i in range(26):
#     abc.append(chr(97 + i) * (i + 1))
# print(abc)

# num = int(input())
# n = 0
# abc = list()
# for i in range(num):
#     n = int(input())
#     abc.append(n ** 3)
# print(abc)

# num = int(input())
# abc = list()
# for i in range(1, num + 1):
#     if num % i == 0:
#         abc.append(i)
# print(abc)


# num = int(input())
# sum_num = list()
# n = int(input())
# n_prev = 0
# for i in range(num - 1):
#     n_prev = n
#     n = int(input())
#     sum_num.append(n_prev + n)
# print(sum_num)


# num = int(input())
# n = 0
# n_list = list()
# for i in range(num):
#     n = int(input())
#     n_list.append(n)
# del n_list[1::2]
# print(n_list)


# num = int(input())
# s_list = list()
# ch_str = ''
# s = ''
# for i in range(num):
#     s = input()
#     s_list.append(s)
# find_ch = int(input())
# for c in s_list:
#     if len(c) > find_ch - 1:
#         ch_str += c[find_ch - 1]
#     else:
#         continue
# print(ch_str)

# num = int(input())
# s_list = list()
# for i in range(num):
#     s = input()
#     s_list.extend(s)
# print(s_list)


# s = ['q', 'w', 't', 'b']
# for i in range(len(s)):
#     print(s[i], end=' ')

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sum_sqr = 0
# for i in numbers:
#     sum_sqr = sum_sqr + i**2
# print(sum_sqr)


# num = int(input())
# f = 0
# l_x = list()
# l_y = list()
# for i in range(num):
#     num = int(input())
#     l_x.append(num)
#     f = num ** 2 + 2 * num + 1
#     l_y.append(f)
# print(*l_x, sep='\n')
# print()
# print(*l_y, sep='\n')


# num = int(input())
# num_list = list()
# for i in range(num):
#     num = int(input())
#     num_list.append(num)
# for j in num_list:
#     if j == max(num_list) or j == min(num_list):
#         continue
#     print(j)

# num = int(input())
# num_list = list()
# for i in range(num):
#     num = int(input())
#     num_list.append(num)
# num_list.remove(max(num_list))
# num_list.remove(min(num_list))
# print(*num_list, sep='\n')

# s_list = list()
# num = int(input())
# for i in range(num):
#     s = input()
#     if s not in s_list:
#         s_list.append(s)
# for j in s_list:
#     print(j)


# s_list = ['A caelo usque ad BEEGEEK centrum',
#           'A capillo usque ad ungues',
#           'A capite ad calcem beegeek',
#           'Ab absurdo beegeeK',
#           'Ab BEEGEEK equis ad asinos',
#           'Ab hoedis scindere oves']
# n_list = list()
# word = 'Beegeek'
# n_word = word.lower()
# for i in s_list:
#     n_list.append(i.lower())
# for j in range(len(n_list)):
#     if n_word in n_list[j]:
#         print(s_list[j])


# n = int(input())
# s_list = list()
# n_list = list()
# for a in range(n):
#     s_list.append(input())
# word = input()
# n_word = word.lower()
# for i in s_list:
#     n_list.append(i.lower())
# for j in range(len(n_list)):
#     if n_word in n_list[j]:
#         print(s_list[j])

# num1 = int(input())
# first_list = list()
# for i in range(num1):
#     first_list.append(input())
#
# num2 = int(input())
# second_list = list()
# for i in range(num2):
#     second_list.append(input())
#
# counter = 0
#
# n_first_list = list()
# for a in first_list:
#     n_first_list.append(a.lower())
#
# n_second_list = list()
# for b in second_list:
#     n_second_list.append(b.lower())
#
# for i in range(len(n_first_list)):
#     for j in range(len(n_second_list)):
#         if n_second_list[j] in n_first_list[i]:
#             counter += 1
#             if counter == len(second_list):
#                 print(first_list[i])
#     counter = 0


# num = int(input())
# num_list = list()
# for i in range(num):
#     num_list.append(int(input()))
# for j in num_list:
#     if j < 0:
#         print(j)
# for j in num_list:
#     if j == 0:
#         print(j)
# for j in num_list:
#     if j > 0:
#         print(j)


# s = input()
# name1 = s.split()
# name2 = list()
# for i in range(len(name1)):
#     name2.extend(name1[i])
# name1 = []
# for j in name2:
#     if j.isupper() == True:
#         name1.append(j)
# print(*name1, sep='.', end='.')


# s = input()
# s_list = s.split("\\")
# for c in s_list:
#     print(c)


# numbers = input().split()
# for i in range(len(numbers)):
#     print(int(numbers[i]) * '*')


# num = input().split('.')
# counter = 0
# for i in range(len(num)):
#     if 0 <= int(num[i]) <= 255:
#         counter += 1
# if counter == 4:
#     print("ДА")
# else:
#     print("НЕТ")

# num_list = list()
# num_list.extend(input())
# sp = input()
# print(sp.join(num_list))

# num_list = input().split()
# count = 0
# for i in range(len(num_list)):
#     for j in range(i + 1, len(num_list)):
#         if num_list[j] == num_list[i]:
#             count += 1
# print(count)


# n_list = [2, 2, 2, 2, 2]
# for i in range(len(n_list)):
#     for j in range(i + 1, len(n_list)):
#         if n_list[j] == n_list[i]:
#             print("YES")


# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers.extend(numbers)
# numbers.insert(3, 25)
# print(numbers)


# s_list = input().split()
# for i in range(len(s_list)):
#     s_list[i] = int(s_list[i])
# if len(s_list) > 1:
#     s_max = max(s_list)
#     s_min = min(s_list)
#     index_s_max = s_list.index(s_max)
#     index_s_min = s_list.index(s_min)
#     s_list.remove(s_max)
#     s_list.remove(s_min)
#     if s_max > 99:
#         s_list.insert(index_s_max - 1, s_min)
#         s_list.insert(index_s_min, s_max)
#     else:
#         s_list.insert(index_s_max, s_min)
#         s_list.insert(index_s_min, s_max)
#     print(*s_list)
# else:
#     print(*s_list)


# s_list = input().split()
# n_list = list()
# for i in range(len(s_list)):
#     s_list[i] = int(s_list[i])
# s_max = max(s_list)
# s_min = min(s_list)
# index_s_max = s_list.index(s_max)
# index_s_min = s_list.index(s_min)
# for i in range(len(s_list)):
#     if s_list[i] == s_max:
#         n_list.append(s_min)
#     elif s_list[i] == s_min:
#         n_list.append(s_max)
#     else:
#         n_list.append(s_list[i])
# print(*n_list)


# s = input().lower()
# s_list = s.split()
#
# print(f"Общее количество артиклей: {s_list.count('a') + s_list.count('an') + s_list.count('the')}")

# df = input()
# num = ''
# l_s = list()
# for i in df:
#     if i == '#':
#         continue
#     else:
#         num += i
# for i in range(int(num)):
#     l_s.append(input())
# for i in range(len(l_s)):
#     if '#' in l_s[i]:
#         ind = l_s[i].rfind('#')
#         for j in range(ind, len(l_s[i])):
#             del j

# print(l_s)


# df_s = input()
# df_s = df_s.replace('#', '')
# df_s = int(df_s.strip())
# s = ''
# for i in range(df_s):
#     s += input() + '\n'
# new_s = ""
# s_list = list()
# s_list.extend(s)
# if '#' in s:
#     ind = s_list.index('#')
#     del s_list[ind - 1:len(s_list)]
# new_s = ''.join(s_list)
# print(new_s.rstrip())

# num = input()
# num = num.replace('#', '')
# num = int(num.strip())
# l_s = list()
# new_s = ""
# ind = 0
# for i in range(num):
#     s = input()
#     if '#' in s:
#         ind = s.index('#')
#         new_s = s.replace(s[ind:len(s)], '')
#     else:
#         new_s = s
#     l_s.append(new_s)
# for i in l_s:
#     print(i.rstrip())


# s = input().split()
# num = list()
# for i in range(len(s)):
#     num.append(int(s[i]))
# num.sort()
# print(*num)
# num.sort(reverse=True)
# print(*num)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
#             'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#             'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in',
#             'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_words = [m[1:len(m)] for m in keywords]
# print(new_words)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class',
#             'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for',
#             'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
#             'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(i) for i in keywords]
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class',
#             'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for',
#             'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
#             'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [i for i in keywords if len(i) >= 5]
# print(lengths)

# palindromes = [i for i in range(100, 1000) if (i // 100) % 10 == i % 10]
#
# print(palindromes)


# num = int(input())
# num_list = [i ** 2 for i in range(1, num + 1)]
# for i in num_list:
#     print(i)

# n = input().split()
# n_list = [int(n[i]) ** 3 for i in range(len(n))]
# print(*n_list)

# # s = input().split()
# n_s = [input() for _ in range(1): print(n_s)]
# # print(*n_s)

# n_s = list()
# s = [input().split() for i in range(1)]
# for i in range(len(s)):
#     n_s.append(s[i])
#     print(*n_s[i], sep='\n')


# print(*(input().replace(' ', '\n') for i in range(1)))

# s = input()
# for i in s:
#     if i.isdigit() == False:
#          s = s.replace(i, '')
# print(s)

# print(*(input().isdigit() for i in range(1) if True))

# s = input().split()
# j = 0
# for i in range(len(s)):
#     j = int(s[i])
#     if j % 2 == 0 and j ** 2 % 10 != 4:
#         print(j ** 2, '', end='')


# print(*(int(i) ** 2 for i in input().split() if int(i)%2 == 0 and int(i) ** 2 % 10 != 4))

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#
# print('Отсортированный список:', a)


# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96,
#      -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6,
#      52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91,
#      44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44,
#      -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75,
#      -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39,
#      38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)


# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# t = 0
# for i in range(n - 1):
#     m = a[i]
#     p = i
#     for j in range(i + 1, n):
#         if m > a[j]:
#             m = a[j]
#             p = j
#     if p != a[i]:
#         t = a[i]
#         a[i] = a[p]
#         a[p] = t
#
# print(a)
# 1. ищу минимальное значение от первого элемента до n-го элемента
# 2. добавляю его в конец списка методом append
# 3. удаляю его первое вхождение методом remove
# 4. n -= 1. Тогда в следующем цикле не буду проверять последний элемент, который туда положила
# 5. Повторяю цикл
# a = [5, 1, 4, 2, 8, 6, 10, 7]
# sort_a = list()
# n = len(a)
# for i in range(n):
#     m = min(a)
#     sort_a.append(m)
#     a.remove(m)
# print(sort_a)


# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:-1]
# print(my_list)

# num = int(input())
# n = list()
# for i in range(2, num + 2, 2):
#     n.append(i)
# print(n)

# num1 = input().split()
# num2 = input().split()
# num3 = list()
# for i in range(len(num1)):
#     num3.append(int(num1[i]) + int(num2[i]))
# print(*num3)

# num1 = input().split()
# sm = 0
# num2 = list()
# for i in range(len(num1)):
#     sm += int(num1[i])
# print(*num1, sep='+', end=f"={sm}")

# s_tel = input().split('-')
# counter_1 = 0
# counter_2 = 0
# for i in range(len(s_tel)):
#     if s_tel[i].isdigit():
#         if len(s_tel) == 3:
#             if s_tel[i].isdigit():
#                 if len(s_tel[0]) == 3 and len(s_tel[1]) == 3 and len(s_tel[2]) == 4:
#                     counter_1 += 1
#         if len(s_tel) == 4:
#             if s_tel[i].isdigit() and int(s_tel[0]) == 7:
#                 if len(s_tel[0]) == 1 and len(s_tel[1]) == 3 and len(s_tel[2]) == 3 and len(s_tel[3]) == 4:
#                     counter_2 += 1
#     else:
#         break
# if counter_1 == 3 or counter_2 == 4:
#     print("YES")
# else:
#     print("NO")

# mx = max((len(i) for i in input().split()))
# print(mx)

# s = input().split()
# new_s = list()
# for i in range(len(s)):
#     t = s[i][0]
#     s[i] = s[i].replace(s[i][0:1], '', 1) + t + 'ки'
# print(*s)

# s = (i.replace(i[0], '', 1) + i[0] + 'ки' for i in input().split())
# print(*s)

# print(*(i.replace(i[0], '', 1) + i[0] + 'ки' for i in input().split()))


# def drow_box():
#     print('*' * 10)
#     for i in range(12):
#         print('*', ' ' * 6, '*')
#     print('*' * 10)
# drow_box()

# def drow_box():
#     for i in range(1, 11):
#         print('*' * i)
# drow_box()

# def drow_box (hight, width):
#     for i in range(hight):
#         print('*' * width)
# drow_box(5, 7)
# drow_box(8, 12)


# def print_triangl (base, fill):
#     for i in range(1, ((fill + 2) // 2)):
#         print(i * base)
#     for i in range(0, ((fill + 2) // 2)):
#         print((((fill + 2) // 2) - i) * base)
#
#
# print_triangl(base = input(), fill = int(input()))

# def print_fio (name, surname, patronymic):
#     s = ''
#     s += surname[0].capitalize()
#     s += name[0].capitalize()
#     s += patronymic[0].capitalize()
#     print(s)
#
# name = input()
# surname = input()
# patronymic = input()
#
# print_fio(name, surname, patronymic)


# def print_digit_sum(num):
#     sm = 0
#     while num > 0:
#         sm += num % 10
#         num //= 10
#     print(sm)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)

# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))


# def days_in_month(mounth):
#     if mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8 or mounth == 10 or mounth == 12:
#         return 31
#     elif mounth == 2:
#         return 28
#     else:
#         return 30
#
# m = int(input())
#
# print(days_in_month(m))

# def get_all_dividers(x):
#     x_l = list()
#     for i in range(1, x + 1):
#         if x % i == 0:
#             x_l.append(i)
#     return x_l
#
# def count_of_dividers(x_l):
#     return len(x_l)
#
# x = int(input())
#
# # print(get_all_dividers(x))
# print(count_of_dividers(get_all_dividers(x)))


# def count_of_symbols(s, c):
#     s_list = list()
#     for i in range(len(s)):
#         if s[i] == c:
#             s_list.append(i)
#     return s_list
#
# s = input()
# c = input()
# print(count_of_symbols(s, c))

# def sort_list(l1 ,l2):
#     for i in range(len(l1)):
#         l1[i] = int(l1[i])
#     for j in range(len(l2)):
#         l2[j] = int(l2[j])
#     l3 = l1 + l2
#     l3.sort()
#     print(l3)
#
# l1 = input().split()
# l2 = input().split()
#
# sort_list(l1, l2)



# def sort_lists(total_list):
#     total_list.sort()
#     return total_list
#
# num = int(input())
# total_list = list()
# s = ''
# for i in range(num):
#     s += input() + ' '
# total_list = s.split()
# total_list = list(map(int, total_list))
# print(sort_lists(total_list))

# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if a >= b + c or b >= c + a or c >= a + b:
#         return False
#     else:
#         return True
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))

# def is_real(x):
#     counter = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             counter += 1
#     if counter == 2:
#         return True
#     else:
#         return False
#
# def is_bigger_then_num(x):
#     if is_real(x):
#         x += 1
#         while is_real(x) == False:
#             x += 1
#         return print(x)
#     else:
#         while is_real(x) == False:
#             x += 1
#         return print(x)
#
# n = int(input())
# is_bigger_then_num(n)


# def more_then_8(pas):
#     if len(pas) > 7:
#         return True
#     else:
#         return False
#
# def is_upper(pas):
#     count = 0
#     for i in range(len(pas)):
#         if ord(pas[i]) in range(65, 91):
#             count += 1
#     if count > 0:
#         return True
#     else:
#         return False
#
# def is_lower(pas):
#     count = 0
#     for i in range(len(pas)):
#         if ord(pas[i]) in range(97, 123):
#             count += 1
#     if count > 0:
#         return True
#     else:
#         return False
#
# def is_digit(pas):
#     count = 0
#     for i in range(len(pas)):
#         if pas[i].isdigit():
#             count += 1
#     if count > 0:
#         return True
#     else:
#         return False
#
# def checker(pas):
#     counter = 0
#     if more_then_8(pas):
#         counter += 1
#     if is_upper(pas):
#         counter += 1
#     if is_lower(pas):
#         counter += 1
#     if is_digit(pas):
#         counter += 1
#     if counter == 4:
#         return True
#     else:
#         return False
#
# s = input()
# print(checker(s))

#######################################

# def str_to_list(word):
#     l = list()
#     for i in word:
#         l.append(i)
#     return l
#
# def compare_words(word1, word2):
#     counter = 0
#     l1 = str_to_list(word1)
#     l2 = str_to_list(word2)
#     if len(l1) == len(l2):
#         for i in range(len(l1)):
#             if l1[i] == l2[i]:
#                 counter += 1
#     else:
#         return False
#     if counter == len(l1) - 1:
#         return True
#     else:
#         return False
#
# s1, s2 = input(), input()
# print(compare_words(s1, s2))


# def str_to_list(s):
#     l = list()
#     for i in s:
#         if i.isspace() or i == '.' or i == ',' or i == '-' or i == '!' or i == '?':
#             continue
#         else:
#             l.append(i.lower())
#     return l
#
# def compare_words(s):
#     l = str_to_list(s)
#     rev_l = list()
#     for i in range(1, len(l) + 1):
#         rev_l.append(l[len(l) - i])
#     if l == rev_l:
#         return True
#     else:
#         return False
#
# s = input()
# print(compare_words(s))


# def a_palindr(x):
#     counter = 0
#     for i in range(len(x)):
#         if x[i] == x[len(x) - 1 - i]:
#             counter += 1
#     if len(x) == counter:
#         return True
#     else:
#         return False
#
# def b_simpl(y):
#     counter = 0
#     for i in range(1, y + 1):
#         if y % i == 0:
#             counter += 1
#     if counter == 2:
#         return True
#     else:
#         return False
#
# def c_even(z):
#     if z % 2 == 0:
#         return True
#     else:
#         return False
#
# s = input().split(':')
# x = s[0]
# y = int(s[1])
# z = int(s[2])
# if len(s) == 3:
#     if a_palindr(x) and b_simpl(y) and c_even(z):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

############################

# def is_correct_bracket(s):
#     counter = 0
#     for i in range(len(s)):
#         if s[i] == '(':
#             counter += 1
#         if s[i] == ')':
#             counter -= 1
#         if counter < 0:
#             return False
#     if counter == 0:
#         return True
#     else:
#         return False
#
# s = input()
# if is_correct_bracket(s):
#     print(True)
# else:
#     print(False)

#############################
# def convert_to_snake(s):
#     n_s = s[0].lower()
#     for i in range(1, len(s)):
#         if s[i].isupper():
#             n_s += '_' + s[i].lower()
#         else:
#             n_s += s[i]
#     return n_s
#
#
# s = input()
# print(convert_to_snake(s))

############################

# def midl_line(x1, y1, x2, y2):
#     a = (x1 + x2) / 2
#     b = (y1 + y2) / 2
#     return a, b
#
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(*midl_line(a, b, c, d))

#############################
# import math
# def get_circle(x):
#     c = 2 * math.pi * x
#     s = math.pi * x ** 2
#     return c, s
#
# x = float(input())
# print(*get_circle(x))

############################
# import math
# def solve(a, b, c):
#     d = b**2 - (4 * a * c)
#     if d > 0:
#         x1 = (-b - math.sqrt(d)) / (2 * a)
#         x2 = (-b + math.sqrt(d)) / (2 * a)
#         if x1 > x2:
#             return x2, x1
#         else:
#             return x1, x2
#     if d == 0:
#         x1 = -b / (2 * a)
#         x2 = -b / (2 * a)
#         if x1 > x2:
#             return x2, x1
#         else:
#             return x1, x2
#     if d < 0:
#         return False
#
# a, b, c = float(input()), float(input()), float(input())
# print(*solve(a, b, c))

#####################################

# def print_tree():
#     n = 8
#     j = 6
#     for i in range(1, n):
#         print(' ' * j, '*' * i + '*' * (i - 1))
#         j -= 1
#     print('*' * 15)
# print_tree()

###################################
#
# def get_shipping_cost(x):
#     first_cost = 1000
#     another_cost = 120
#     if x == 1:
#         total_cost = first_cost
#     else:
#         x -= 1
#         total_cost = first_cost + (another_cost * (x))
#     return total_cost
#
# x = int(input())
# print(get_shipping_cost(x))

################################

# import math
#
# def compute_binom(n, k):
#     b = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
#     return int(b)
# x, y = int(input()), int(input())
# print(compute_binom(x, y))

##############################

# def number_to_word(x):
#     f_d = x // 10
#     s_d = x // 100
#     zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
#                            'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
#                            'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один',
#                            'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть',
#                            'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один',
#                            'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть',
#                            'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два',
#                            'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь',
#                            'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три',
#                            'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь',
#                            'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два',
#                            'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть',
#                            'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один',
#                            'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть',
#                            'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один',
#                            'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять',
#                            'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять',
#                            'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре',
#                            'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь',
#                            'девяносто девять']
#
#     if 0 < x < 10:
#         return zero_to_ninety_nine[x]
#     else:
#         return zero_to_ninety_nine[x]
#
# num = int(input())
# print(number_to_word(num))
##################################################
# def get_month(s, x):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#
#     if s == 'ru':
#         return lng_ru[x -1]
#     if s == 'en':
#         return lng_en[x - 1]
# lang = input()
# n = int(input())
# print(get_month(lang, n))

###########################################

# def is_magic(s):
#     date = list()
#     date = s.split('.')
#     if int(date[0]) * int(date[1]) == int(date[2]) % 100:
#         return True
#     else:
#         return False
#
# date = input()
# if is_magic(date):
#     print(True)
# else:
#     print(False)

# def to_list(s):
#     ready_s = list()
#     for i in range(len(s)):
#         if s[i].isspace():
#             continue
#         elif s[i] in ready_s:
#             continue
#         else:
#             ready_s += s[i].lower()
#     return ready_s
#
# def count_letters(ready_s):
#     count = 0
#     new_s = to_list(s)
#     new_s.sort()
#     for i in range(len(new_s)):
#         if ord(new_s[i]) in range(97, 123):
#             count += 1
#     if count == 26:
#         return True
#     else:
#         return False
#
# s = input()
# print(count_letters(s))