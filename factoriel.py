def factoriel(a):
    fact = 1
    if a== 0:
        return 1
    for i in range(1,a+1):
        fact *= i
    print (fact)

factoriel(10)
