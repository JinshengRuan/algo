class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

    def diff(self):
        return self.weight - self.length

    def div(self):
        return float(self.weight) / self.length

def partitionJobsByDiff(jobs, l, r):
    p = jobs[l]
    i = l + 1
    for j in range(l+1, r+1):
        if jobs[j].diff() > p.diff():
            jobs[i], jobs[j] = jobs[j], jobs[i]
            i += 1
        elif jobs[j].diff() == p.diff():
            if jobs[j].weight > p.weight:
                jobs[i], jobs[j] = jobs[j], jobs[i]
                i += 1
    jobs[l], jobs[i-1] = jobs[i-1], jobs[l]
    return i-1

def partitionJobsByDiv(jobs, l, r):
    p = jobs[l]
    i = l + 1
    for j in range(l+1, r+1):
        if jobs[j].div() > p.div():
            jobs[i], jobs[j] = jobs[j], jobs[i]
            i += 1
    jobs[l], jobs[i-1] = jobs[i-1], jobs[l]
    return i-1

def sortJobsByDiff(jobs, l, r):
    if l < r:
        q = partitionJobsByDiff(jobs, l, r)
        sortJobsByDiff(jobs, l, q - 1)
        sortJobsByDiff(jobs, q + 1, r)

def sortJobsByDiv(jobs, l, r):
    if l < r:
        q = partitionJobsByDiv(jobs, l, r)
        sortJobsByDiv(jobs, l, q - 1)
        sortJobsByDiv(jobs, q + 1, r)

def scheduleByDiff(jobs):
    jobs_num = len(jobs)
    sortJobsByDiff(jobs, 0, jobs_num - 1)
    sum_of_weight = 0
    complete = 0
    for i in range(jobs_num):
        complete += jobs[i].length
        sum_of_weight += jobs[i].weight * complete
    return sum_of_weight

def scheduleByDiv(jobs):
    jobs_num = len(jobs)
    sortJobsByDiv(jobs, 0, jobs_num - 1)
    sum_of_weight = 0
    complete = 0
    for i in range(jobs_num):
        complete += jobs[i].length
        sum_of_weight += jobs[i].weight * complete
    return sum_of_weight

def main():
    infile = open('jobs.txt', 'r')
    jobs = []
    infile.readline()
    lines = infile.readlines()
    for line in lines:
        weight, length = line.split()
        jobs.append(Job(int(weight), int(length)))
    print scheduleByDiff(jobs)
#    print scheduleByDiv(jobs)

import sys

if __name__ == '__main__':
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    main()
