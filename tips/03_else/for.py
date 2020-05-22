start = 0
end = 10
break_point = 5

for i in range(start, end):
    print(i)
    if i == break_point:
        break
else:
    print('Nothing')
