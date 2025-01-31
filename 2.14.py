import math
#a)
def f(n):
    sum = 0 # 1
    for i in range(1,n+1): # n+1
        sum += i # 2
    return sum
# 2(n+1)+1
#Асимптотична складність: O(n)

#b)
def f(n):
    sum = 0 #1
    for i in range(1, n+1): # n+1
        sum += i*i # 3
    return sum
#Асимптотична складність: O(n)

#c)
def f(n, a):
    sum = 0 # 1
    for i in range(1, n+1): # n+1
        sum += a**i # 3
    return sum
#Асимптотична складність: O(n)

#d)
def f(n):
    sum = 0 # 1
    for i in range(1, n+1): # n+1
        sum += i**i # n/2
    return sum
#Асимптотична складність: O(n^2)

#e)
def f(n):
    result = 1 # 1
    for i in range(1, n+1): # n
        result *= 1/(1+i) # 4
    return result
#Асимптотична складність: O(n)

#f)
def f(n):
    result = 1 # 1
    for i in range(1, n+1): # n
        result *= 1/(1+math.factorial(i)) # 5
    return result
#Асимптотична складність: O(n)

#g)
def f(n):
    result = 1 # 1
    for i in range(1, n+1): # n
        result *= (a**i)/(1+math.factorial(i)) # 6
    return result
#Асимптотична складність: O(n)

#h)
def f(n):
    result = 1 # 1
    for i in range(1, n+1): # n
        result *= 1/(1+1**m) # m + 5
    return result
# (m+5)n + 1
#Асимптотична складність: O(mn)

#i)
def f(n):
    result = 1 # 1
    for i in range(1, n+1): # n
        result *= 1/(1+i**i) # n/5
    return result
#Асимптотична складність: O(n^2)