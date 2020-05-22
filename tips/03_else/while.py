start = 0
end = 10
break_point = 5

i = start

while i < end:
    print(i)
    i += 1
    if i == break_point:
        break
else:
    print('Nothing')
