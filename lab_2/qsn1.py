from collections import deque


def BFS(ja, jb, target):
    m = {}
    isSolvable = False
    path = []
    q = deque()
    q.append((0, 0))  # initial state

    while (len(q) > 0):
        u = q.popleft()
# check if this state is visited
        if (((u[0], u[1]) in m)):
            continue
# check if this state is valid
        if ((u[0] > ja or u[1] > jb or u[0] < 0 or u[1] < 0)):
            continue
        path.append([u[0], u[1]])  # add current state to path
        m[(u[0], u[1])] = 1  # mark current state as visited

        if (u[0] == target or u[1] == target):
            isSolvable = True
        if (u[0] == target):
            if (u[1] != 0):
                path.append([u[0], 0])

            else:

                if (u[0] != 0):
                    path.append([0, u[1]])

# printing result:
                    sz = len(path)
                    for i in range(sz):
                        print("(", path[i][0], ",",
                              path[i][1], ")")
                    break
# if we are not getting solution yet, we need to expand to the next child

    q.append((u[0], jb))  # fill jug 1
    q.append((ja, u[1]))

    for ap in range(max(ja, jb)+1):
        # pour ap amount from jug 2 to 1
        c = u[0]+ap
        d = u[1] - ap
# check its validity as new state
        if (c == ja or (d == 0 and d >= 0)):
            q.append([c, d])
# pour ap amount from jug1 to 2
            c = u[0] - ap
            d = u[1]+ap
    if ((c == 0 and c >= 0) or d == jb):
        q.append([c, d])
# empty jug 1 and 2
        q.append([ja, 0])
        q.append([0, jb])
    if (not isSolvable):
        print("No solution possible.")


# driver code
if __name__ == '__main__':
    myJug1, myJug2, myTarget = 4, 3, 2
    print("solution of water jug problem is:\n")
    BFS(myJug1, myJug2, myTarget)
