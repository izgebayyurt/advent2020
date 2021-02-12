def main():

    # seats
    seats = []

    # read the file
    fp = open("advent13.txt")
    time = int(fp.readline())

    bus_times = fp.readline().strip().split(',')

    new_bus_times = []
    bus_idx = []

    for i in range(len(bus_times)):
        if bus_times[i] != 'x':
            new_bus_times.append(int(bus_times[i]))
            if i != 0:
                bus_idx.append(i)
        else:
            new_bus_times.append(bus_times[i])

    bus_times = new_bus_times

    base_num = bus_times[0]

    target_num = bus_times[0]

    # print( (17 * 41 * 643 * 23 * 13 * 29 * 433 * 37) * -13 )


    # print(1182922135469659 - 809367776900293)

    # print(373554358569366 - 54)
    
    print(373554358569366 % 41)

    # print(target_num)


if __name__ == "__main__":
    main()
    