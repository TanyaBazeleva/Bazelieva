import time
n = 1000000

start = time.time()
#a)
k += 1  # 2
i = n   # 1
while i > 0: # n+1
    i -= 1  # 2
# 2*n + 1 + 2 = 2n + 3

#b)
i = n  # 1
while i > 1:  # log2(n)+1
    k += 1  # 2
    i //= 2  # 2
# 4*log2(n) + (log2(n)+1) + 1 = 5log2(n) +2

#c)
i = 0  # 1
while i < n:  # n/2 + 1
    j = 0  #1
    while j < n:  # n/2 + 1
        k += 1  # 2
        j += 2  # 2
    # 4*(n/2) + n/2 + 1
    i += 2  # 2
    # 4*(n/2) + n/2 + 1 + 2
#  (5*(n/2) + 3 + 1)*(n/2) + n/2 + 1 +1 = 5/4*(n^2) + 5/2*(n) +2

#d)
i = 0  # 1
while i < n:  # n + 1
    j = 0   # 1
    while j < i * i:  # i^2 + 1
        k += 1  # 2
        j += 1  # 2
    #  sum_{i=1}^4*(i^2) + i^2 + 1
    i += 1  # 2
    #  sum_{i=1}^4*(i^2) + i^2 + 1 + 2
# (sum_{i=1}^4*(i^2) + i^2 + 3 + 1)*n + n+1 + 1 = 5*(i^2)*n + 5*n + 1

#e)
i = 1  # 1
while i < n:  # log2(n) + 1
    j = 1  #1
    while j < n:  # log2(n)  + 1
        k += 1  # 2
        j *= 2  # 2
    #  4*log2(n) + log2(n) + 1
    i *= 2  # 2
    #  4*log2(n) + log2(n) + 1 + 2
# (5*log2(n) + 3 + 1)*log2(n) + log2(n)+1 + 1

#f)
i = 1  # 1
while i < n:  # log2(n) + 1
    j = i  #1
    while j < n:  # log2(n/i)  + 1
        k += 1  # 2
        j *= 2  # 2
    #  sum_{i=1}^{\log_2(n)} * 4*log2(n/i) + log2(n/i) + 1
    i *= 2  # 2
    #  sum_{i=1}^{\log_2(n)} * 4*log2(n/i) + log2(n/i) + 1 + 2
# (sum_{i=1}^{\log_2(n)} * 4*log2(n/i) + log2(n/i) + 3 + 1)*log2(n) + log2(n)+1 + 1

end = time.time()
print((end - start)/n)