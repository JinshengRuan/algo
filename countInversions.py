def countSplitInversions(B, C):
    D = []
    i = 0
    j = 0
    num = 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            num = num + len(B) - i

    if i < len(B):
        D.extend(B[i:])
    if j < len(C):
        D.extend(C[j:])

    return (D, num)

def countInversions(A):
    n = len(A)
    if n == 1:
        return (A,0)
    else:
        mid = n // 2
        (B,x) = countInversions(A[:mid])
        (C,y) = countInversions(A[mid:])
        (D,z) = countSplitInversions(B, C)
        return (D,x+y+z)

def main():
    integers = []
    infile = open('IntegerArray.txt', 'r')
    for line in infile:
        integers.append(int(line))
    print integers
    
    (dummy, num) = countInversions(integers)
    print num
    return

if __name__ == '__main__':
    main()
