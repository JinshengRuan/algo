def main():
    nums = {}
    infile = open('algo1-programming_prob-2sum.txt','r')
    lines = infile.readlines()
    for line in lines:
        nums[int(line)] = int(line)

    print 'all in dict'

    count = 0
    for t in range(-10000,10001):
        for x in nums.keys():
            if ((t - x) in nums) and ((t - x) != x):
                count = count + 1
                break

    print count

if __name__ == '__main__':
    main()
            
