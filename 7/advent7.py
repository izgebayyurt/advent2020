
def main():

    bag_dict = {}

    fp = open("advent7.txt")
    line = fp.readline()

    line_count = 0

    while line != "":

        line_count+=1

        words = line.split(" ")
        name = ""
        for word in words:
            if word == "bags":
                break
            name += word
        bag_dict[name] = []

        read = False
        inner_bag = ""
        for word in words:
            word = word.strip()
            if read and word != "bags," and word != "bags." and word != "bag." and word != "bag,":
                inner_bag += word
            
            if word == "bags," or word == "bags." or word == "bag," or word == "bag.": 
                bag_dict[name].append(inner_bag)
                inner_bag = ""
                read = False

            if word == "1" or word == "2" or word == "3" or word == "4" or word == "5":
                read = True
                inner_bag += word
        
        line = fp.readline()
    
    inner_bags = []
    counted_bags = []
    
    for bag in bag_dict["shinygold"]:
        for _ in range(int(bag[0])):
            inner_bags.append(bag[1:])

    print(inner_bags)

    for inner_bag in inner_bags:
        for bag in bag_dict[inner_bag]:
            if bag != "":
                for _ in range(int(bag[0])):
                    inner_bags.append(bag[1:])

    print(len(inner_bags))

    # done = False
    # while not done:
    #     done = True
    #     for key in bag_dict.keys():
    #         for bag in bag_dict[key]:
    #             if (bag in outer_bags) and (key not in counted_bags):
    #                 done = False
    #                 counted_bags.append(key)
    #                 outer_bags.append(key)

    # print(len(outer_bags))

if __name__ == "__main__":
    main()