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

# num_list = list()
# num_list.extend(input())
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




