a = [3, 17, 6, 12, 3, 56, 43]

if a[0] > a[1]:
    max1, max2 = a[0], a[1]
else:
    max1, max2 = a[1], a[0]

for x in a[2:]:
    if x > max1:
        max1, max2 = x, max1
    else:
        if x > max2:
            max2 = x

print(max2)
