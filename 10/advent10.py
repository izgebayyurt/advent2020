
'''
    For any number n (length of 1-chain), return the number of possible paths that can be taken to traverse that path.
'''
# this is a function similar to fibonnaci series. starts with 0 1 1 and the next number is the sum of previous 3 numbers.
# perhaps there is a nicer way to do this, but i did it linearly. this gives us for an
def paths(n):
    multipliers = [0, 1, 1]
    num = 1
    
    if n == 0:
        return 1
    while num != n:
        sum = multipliers[-1] + multipliers[-2] + multipliers[-3]
        multipliers.append(sum)
        num += 1

    return multipliers[-1]

def main():

    # jolt list
    jolts = []

    # read the file
    fp = open("advent10.txt")
    line = fp.readline()

    while line != "":
        jolts.append(int(line))
        line = fp.readline()

    # add the 0 for starting
    jolts.append(0)

    # sort the entries
    jolts.sort()

    # list for the differences
    jolt_dif = []

    # take the differences of each entry and add it to the list
    '''
    For example, if the jolts is 0 1 2 3 6 7 8, we get 1 1 1 3 1 1
    '''

    for i in range(len(jolts)-1):
        jolt_dif.append(jolts[i+1]-jolts[i])

    # now we just need to find out the ways for each consecutive 1's
    '''
    The idea here is 0-1-2-3 has 4 different ways of being traversed, 
    3->6 is a mandatory jump, and 6-7-8 can be traversed 2 different ways. 
    Thus, 3's in our difference list signals a break in 1-chains.
    '''

    # the list to keep track of 1-chains
    ways = []
    # current consecutive ones (starting with 0)
    consecutive_ones = 0

    # loop over each difference number
    for num in jolt_dif:
        if num == 1: # if the number is 1, increment the chain
            consecutive_ones += 1
        if num == 3: # if the number is 3, break the chain and add the possible paths using helper function
            ways.append(paths(consecutive_ones))
            consecutive_ones = 0

    # finally, making sure that we count the final chain
    if consecutive_ones != 0:
        ways.append(paths(consecutive_ones))


    # now we just multiply every number    
    res = 1

    for i in ways:
        res *= i

    # and print the result
    print(res)

if __name__ == "__main__":
    main()
    