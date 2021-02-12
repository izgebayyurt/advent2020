# runtime, 45 secs
def main():
    starting_nums = [2,0,6,12,1,3]
    num_dict = {2:[0], 0:[1], 6:[2], 12:[3], 1:[4], 3:[5]}
    current_num = starting_nums[-1]

    for i in range(6, 30000000):
        if current_num in num_dict.keys():
            if len(num_dict[current_num]) > 1:
                current_num = num_dict[current_num][-1] - num_dict[current_num][-2]
                if current_num in num_dict.keys():
                    if len(num_dict[current_num]) > 1:
                        num_dict[current_num][0] = num_dict[current_num][1]
                        num_dict[current_num][1] = i
                    else:
                        num_dict[current_num].append(i)
                else:
                    num_dict[current_num] = [i]
            else:
                current_num = 0
                num_dict[current_num].append(i)

        else:
            current_num = 0
            num_dict[current_num] = [i]

    print(current_num)

# runtime, 9 secs, wastes a lot of memory though.
def main2():
    starting_nums = [2,0,6,12,1,3]

    num_dict = [-1 for i in range (30000000)]

    for i in range(len(starting_nums)-1):
        num_dict[starting_nums[i]] = i

    current_num = starting_nums[-1]

    for i in range(5, 30000000-1):
        
        if num_dict[current_num] != -1:
            
            save_current_num = i - num_dict[current_num]
            num_dict[current_num] = i
            current_num = save_current_num

        else:
            num_dict[current_num] = i
            current_num = 0


    print(current_num)
    

# main()
main2()