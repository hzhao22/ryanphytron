print ("Hail Stone")
#Starting with any positive whole number $n$ form a sequence in the following way:
#If $n$ is even, divide it by $2$ to give $n^\prime = n/2$.
#If $n$ is odd, multiply it by $3$ and add $1$ to give $n^\prime = 3n + 1.$


def hailStone(n):
    numbers = []
    while ( 1 not in numbers):
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        numbers.append(int(n))
    return numbers

for i in range(1, 31):
    mylist = hailStone(i)
    print(i, len(mylist), max(mylist))



