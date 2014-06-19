class MaxHeap:
    def __init__(self):
        self.A = []
        self.size = 0

    def max_heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.size and self.A[r] > self.A[largest]:
            largest = r
        if i != largest:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def insert(self, n):
        if len(self.A) <= self.size:
            self.A.append(n)
            self.size += 1
        else:
            self.size += 1
            self.A[self.size - 1] = n

        i = self.size - 1
        parent = (i - 1) // 2
        while i > 0 and self.A[i] > self.A[parent]:
            self.A[i], self.A[parent] = self.A[parent], self.A[i]
            i = parent
            parent = (i - 1) // 2

    def extract_max(self):
        if self.size < 1:
            return None
        max = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return max

    def max(self):
        return self.A[0]


class MinHeap:
    def __init__(self):
        self.A = []
        self.size = 0

    def min_heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r < self.size and self.A[r] < self.A[smallest]:
            smallest = r
        if i != smallest:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.min_heapify(smallest)

    def insert(self, n):
        if len(self.A) <= self.size:
            self.A.append(n)
            self.size += 1
        else:
            self.size += 1
            self.A[self.size - 1] = n

        i = self.size - 1
        parent = (i - 1) // 2
        while i > 0 and self.A[i] < self.A[parent]:
            self.A[i], self.A[parent] = self.A[parent], self.A[i]
            i = parent
            parent = (i - 1) // 2

    def extract_min(self):
        if self.size < 1:
            return None
        min = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return min

    def min(self):
        return self.A[0]

def main():
    maxheap = MaxHeap()
    minheap = MinHeap()
    medians = []
    total = 0
    infile = open('Median.txt', 'r')
    lines = infile.readlines()
    for line in lines:
        num = int(line)
        if total % 2 == 0:
            maxheap.insert(num)
            total += 1
        
            if minheap.size > 0:
                if maxheap.max() > minheap.min():
                    toMin = maxheap.extract_max()
                    toMax = minheap.extract_min()
                    maxheap.insert(toMax)
                    minheap.insert(toMin)
        
        else:
            maxheap.insert(num)
            toMin = maxheap.extract_max()
            minheap.insert(toMin)
            total += 1

        median = maxheap.max()
        medians.append(median)

    sum = 0
    for m in medians:
        sum += m
        
    print sum % 10000

if __name__ == '__main__':
    main()
