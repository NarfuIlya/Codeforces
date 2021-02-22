n = int(input())

for i in range(n):
    t = int(input())
    if t == 2:
        print("1 1")
    elif t % 2 == 1:
        print("{} 1".format(t-1))
    else:
        print("{} 2".format(t-2))