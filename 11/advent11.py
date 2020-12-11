def getNeighbors(i,j,seats):
    i_idx = [i-1, i, i+1]
    j_idx = [j-1, j, j+1]
    neighbors = []

    for i_ in i_idx:
        for j_ in j_idx:
            if i_ < 0 or j_ < 0:
                continue
            if i_ >= len(seats) or j_ >= len(seats[0]):
                continue
            if i_ == i and j_ == j:
                continue

            neighbors.append(seats[i_][j_])

    return neighbors

def getNeighbors2(i,j,seats):

    occupied_neighbors = []

    # left
    i_ = i
    j_ = j
    while i_ > 0:
        i_ -= 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    # right
    i_ = i
    j_ = j
    while i_ < len(seats)-1:
        i_ += 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    # up
    i_ = i
    j_ = j
    while j_ > 0:
        j_ -= 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    # down
    i_ = i
    j_ = j
    while j_ < len(seats[0])-1:
        j_ += 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    ##############

    # left & up
    i_ = i
    j_ = j
    while i_ > 0 and j_ > 0:
        i_ -= 1
        j_ -= 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    # right & up
    i_ = i
    j_ = j
    while i_ < len(seats)-1 and j_ > 0:
        i_ += 1
        j_ -= 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    # left & down
    i_ = i
    j_ = j
    while i_ > 0 and j_ < len(seats[0])-1:
        i_ -= 1
        j_ += 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    # right & down
    i_ = i
    j_ = j
    while i_ < len(seats)-1 and j_ < len(seats[0])-1:
        i_ += 1
        j_ += 1 
        if seats[i_][j_] == '#':
            occupied_neighbors.append('#')
            break
        if seats[i_][j_] == 'L':
            occupied_neighbors.append('L')
            break

    
    return occupied_neighbors
    

def main():

    # seats
    seats = []

    # read the file
    fp = open("advent11.txt")
    line = fp.readline()

    while line != "":
        row = []
        for i in line:
            if i != "\n":
                row.append(i)
        seats.append(row)
        line = fp.readline()

    '''
        Test code to check whether getNeighbors work
    '''
    # for i in range(len(seats)):
    #     for j in range(len(seats[0])):
    #         getNeighbors(i,j,seats)



    changed = True
    while changed:

        changed = False

        # we are changing all at once so create a new grid
        new_seats = [[0 for i in range(len(seats[0]))] for i in range(len(seats))]

        for i in range(len(seats)):
            for j in range(len(seats[0])):

                # get neighbors
                neighbors = getNeighbors2(i,j,seats)

                # count the occupied seats
                occupied_count = 0
                for neighbor in neighbors:
                    if neighbor == '#':
                        occupied_count += 1

                # rules       
                if seats[i][j] == 'L' and '#' not in neighbors:
                    new_seats[i][j] = '#'
                    changed = True
                elif seats[i][j] == '#' and occupied_count >= 5:
                    new_seats[i][j] = 'L'
                    changed = True
                else:
                    new_seats[i][j] = seats[i][j]

        seats = new_seats

    # count the final occupied seats
    occupied_count = 0

    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == '#':
                occupied_count += 1

    print(occupied_count)
    

if __name__ == "__main__":
    main()
    