print ("Hail Stone")
#Starting with any positive whole number $n$ form a sequence in the following way:
#If $n$ is even, divide it by $2$ to give $n^\prime = n/2$.
#If $n$ is odd, multiply it by $3$ and add $1$ to give $n^\prime = 3n + 1.$


def hailStone(n):
    numbers = []
    while (n != 1):
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        numbers.append(n)
    return numbers

print(hailStone(50))



