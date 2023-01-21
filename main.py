def myMax(list2):
    max = list2[0]
    for x in list2:
        if x > max:
            max = x
    return max

list2 = []
n = int(input())
for i in range(0, n):
    ele = int(input())
    list2.append(ele)

print(myMax(list2))
