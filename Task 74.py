
def fac(m):
    if m == 0 or m == 1:
        return 1
    f = 1
    for i in range(1, m + 1):
        f *= i
    return f

def end(k):
    s = str(k)
    sum = 0
    for i in s:
        sum += fac(int(i))
    return sum

B = {1 : 1, 2 : 1, 145 : 1}

def glav(n):
    ap = n
    if n in B:
        return B[n]
    else:
        lst = []
        lst.append(n)
        nn = A[n]
        
        count = 1
        while nn not in lst:
            lst.append(nn)
            n = nn
            nn = A[n]
            count += 1
        B[ap] = count
        return count
            
        

A = dict()

for j in range(1, 2200000):
    A[j] = end(j)

print("End first part")

score = 0

for i in range(3, 1000000):
    if glav(i) == 60:
        score += 1
        
print(score)

print("End")
