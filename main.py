num = int(input())
flag = True
for i in range(2, num):
    if num % 2 == 0:
        flag = False
        break

if flag == True:
    print("Simple number")
else:
    print("Combined number")