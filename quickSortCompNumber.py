def chooseFirst(A, l, r):
    return

def chooseLast(A, l, r):
    A[l], A[r] = A[r], A[l]

def chooseMed(A, l, r):
    m = (r - l) // 2 + l
    if (A[l] > A[m] and A[l] < A[r]) or (A[l] < A[m] and A[l] > A[r]):
        return
    elif (A[m] > A[l] and A[m] < A[r]) or (A[m] < A[l] and A[m] > A[r]):
        A[m], A[l] = A[l], A[m]
        return
    elif (A[r] > A[l] and A[r] < A[m]) or (A[r] < A[l] and A[r] > A[m]):
        A[r], A[l] = A[l], A[r]
        return

    
def partition(A, l, r):
##    chooseFirst(A, l, r)
##    chooseLast(A, l, r)
    chooseMed(A, l, r)
    p = A[l]
    i = l + 1
    for j in range(l+1,r+1):
        if A[j] < p:
            A[i],A[j] = A[j],A[i]
            i = i+1
    A[l],A[i-1] = A[i-1],A[l]
    return i - 1

def countCompNum(A, l, r):
    if l >= r:
        return 0
    else:
        q = partition(A, l, r)
        return r - l + countCompNum(A, l, q - 1) + countCompNum(A, q + 1, r)
        
def main():
    integers = []
    infile = open('QuickSort.txt', 'r')
    for line in infile:
        integers.append(int(line))
##    print integers

    num = countCompNum(integers, 0, len(integers) - 1)
##    print integers
    print num
    return

if __name__ == '__main__':
    main()
