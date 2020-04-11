import time
a = 0
b = 0
s = 0


def test_g(l):                      # Check whether the passed list is goal or not and return                        
    if l == g:
        return True
    return False


# By comparing current list with visited list it has to be checked if the state has been visited before
def test_v(test_l, b, d):
    global a
    global s
    if test_l in v:
        pass
    else:
        queue.append(test_l)
        a += 1
        bfs_dict[a] = [b, d]
        # if state is new, append the parent node number b and move character d to the bfs_dictionary
        if test_g(test_l):
            s = a


def lt(l_l, j, b):
    if j in {0, 4, 8, 12}:                                      # skip left operation when 0 is in the extreme left,
        pass
    else:
        l_l[j - 1], l_l[j] = l_l[j], l_l[j - 1]     # swap 0 with its left neighbour
        test_v(l_l[:], b, d='L')


def rt(r_l, j, b):
    if j in {3, 7, 11, 15}:                                     #skip right operation if 0 is in the extreme right
        pass
    else:
        r_l[j + 1], r_l[j] = r_l[j], r_l[j + 1]     # swap 0 with its right neighbour
        test_v(r_l[:], b, d='R')


def up(u_l, j, b):
    if j in {0, 1, 2, 3}:                                       # if 0 is in the extreme top, skip up operation
        pass
    else:
        u_l[j - 4], u_l[j] = u_l[j], u_l[j - 4]     # swap 0 with its upper neighbour
        test_v(u_l[:], b, d='U')


def dn(d_l, j, b):
    if j in {12, 13, 14, 15}:                                   # if 0 is in the extreme bottom, skip down operation
        pass
    else:
        d_l[j + 4], d_l[j] = d_l[j], d_l[j + 4]     # swap 0 with its lower neighbour
        test_v(d_l[:], b, d='D')


def bfs():                                                      # main function
    global b
    bfs_dict[0] = [None, '']
    queue.append(m_l)
    while len(queue) > 0:                                       # check if queue is empty
        v.append(queue[0])                                # append the first list in queue to the visited list
        if test_g(queue[0]):                                # check if goal is found or not and print output accordingly
            print("Goal state found!")
            move = [bfs_dict[save][1]]
            f = bfs_dict[s][0]
            while bfs_dict[f][0] is not None:
                move.append(bfs_dict[f][1])
                f = bfs_dict[f][0]
           
            print("Number of Nodes expanded:", len(v))
            end = time.time()
            print("Time Taken:", end - start, "seconds")        # if time > 0.1 s
            
            break
        else:
            j = queue[0].index(0)                               # find index of the location of 0
            lt(queue[0][:], j, b)                             # perform left-shift operation
            rt(queue[0][:], j, b)                            # perform right-shift operation
            up(queue[0][:], j, b)                               # perform top-shift operation
            dn(queue[0][:], j, b)                             # perform bottom-shift operation
            b += 1
            queue.pop(0)
            mid = time.time()
            if (mid - start) > 10.0:                            # stop if the bfs takes more than 10 seconds
                print("solution is not found")
                return


ip = input("Enter input state: ")                              # get the input
m_l = list(map(int, ip.split()))                            # convert to int and put into a list
start = time.time()                                            # start process timer after the input has been taken
v = []
queue = []
bfs_dict = {}
g = [0, 3, 2, 5, 4, 7, 6, 8, 9, 11, 10, 12, 15, 14, 13,1]  # goal state
bfs()
