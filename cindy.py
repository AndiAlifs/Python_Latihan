a = int(input("X = "))
prima = True
if (a >= 2):
    for i in range (2,a):
        if (a % i) == 0:
            prima = False
    if (prima):
        print ( a, "bilangan prima")
    else:
        print ( a, "bukan bilangan prima")
else:
    print ( a, "bukan bilangan prima")
