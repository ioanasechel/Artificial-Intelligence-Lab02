import sys


def tsp_solve(n, tsp, source, destination):
    pass


def find_min_route(tsp):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = sys.maxsize
    visitedRouteList = [0]
    route = [0] * len(tsp)

    while i < len(tsp) and j < len(tsp[i]):
        if counter >= len(tsp[i]) - 1:
            break
        if j != i and j not in visitedRouteList:
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1
        j = j + 1

        if j == len(tsp[i]):
            sum += min
            min = sys.maxsize
            visitedRouteList.append(route[counter] - 1)
            j = 0
            i = route[counter] - 1
            counter = counter + 1

    i = route[counter - 1] - 1
    for j in range(len(tsp)):
        if i != j and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1
    sum += min
    route.sort()
    return route, sum
    # print(route)
    # print("Minimum cost is: ", sum)


def main():
    # tsp = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    # tsp2 = [[0, 1, 2, 4], [1, 0, 3, 15], [2, 3, 0, 6], [4, 15, 6, 0]]
    # find_min_route(tsp)
    # find_min_route(tsp2)

    f = open("C:/Users/ioana/OneDrive/Documents/Facultate/Semestrul 4/Inteligenta "
             "artificiala/Laborator/Artificial-Intelligence-Lab2/in.txt", 'r')
    fout = open("C:/Users/ioana/OneDrive/Documents/Facultate/Semestrul 4/Inteligenta "
                "artificiala/Laborator/Artificial-Intelligence-Lab2/out.txt", 'w')

    l = [[int(num) for num in line.split(',')] for line in f]
    n = l[0][0]
    source = l[n + 1][0]
    destination = l[n + 2][0]
    l.pop(0)
    l.pop(n)
    l.pop(n)

    # print(l, source, destination)
    rez = find_min_route(l)
    fout.write("%i\n" % n)
    for i in rez[0]:
        fout.write("\n".join([str(i) + ","]))
    fout.write("\n%i\n" % rez[1])


main()