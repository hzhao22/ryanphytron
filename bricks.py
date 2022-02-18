def make_bricks(small, big, goal):
    if (big == 0) and goal > small:
        return False;
    if (big == 0) and goal <= small:
        return True;

    if (small == 0 and goal % 5 != 0):
        return False;
    if (small == 0 and goal % 5 == 0):
        return True;

    # if (goal % big > small):
    #    return False;

    print("goal//5", goal//5)
    if (goal // 5 >= big and goal - big * 5 > small):
        print(1111111111)
        return False;

    if (goal // 5 < big and goal - goal // 5 * 5 > small):
        print(222222222)
        return False;



    print(33333333333)

    return True

make_bricks(1,4,11)