# choosing the next node to be visited
def choose_node(visited, matrix):
    min = 1000000
    r = 0
    for y in range(len(matrix)):
        if visited[y] == 0 and matrix[y] < min:
            min = matrix[y]
            r = y
    return r


# generic function that returns both solutions
def search_path(x, matrix, x1, y1):
    visited = [0] * len(matrix)
    xr = x + 1
    list = [xr]
    visited[x] = 1
    i = 1
    d = 0

    path_list_x1_y1 = []
    d2 = 0
    elem = -1
    elem1 = -1
    if xr == x1:
        path_list_x1_y1.append(xr)
        elem = y1
        elem1 = 1
    if xr == y1:
        path_list_x1_y1.append(xr)
        elem = x1
        elem1 = 2

    while i != len(matrix):
        y = choose_node(visited, matrix[x])
        yy = y + 1
        list.append(yy)
        visited[y] = i
        d = d + matrix[x][y]

        if elem == -1 and (y1 == yy or x1 == yy):
            path_list_x1_y1.append(yy)
            if y1 == yy:
                elem = x1
                elem1 = 2
            else:
                elem = y1
                elem1 = 1
        elif elem != -1 and elem != -2:
            path_list_x1_y1.append(yy)
            d2 = d2 + matrix[x][y]
            if elem == yy:
                elem = -2

        x = y
        i = i + 1
    if elem1 == 2:
        path_list_x1_y1.reverse()
    return list, d, path_list_x1_y1, d2


def solve(matrix, x1, y1):
    minimal_path = 9999999999
    minimal_path_list = []
    minimal_path_2 = 9999999999
    minimal_path_list_sd = []

    # searching for both minimum paths through the whole matrix
    for i in range(len(matrix)):
        l, d, l2, d2 = search_path(i, matrix, x1, y1)
        d = d + matrix[i][l[len(l) - 1] - 1]
        # print(l)
        # print(d)
        if d < minimal_path:
            minimal_path = d
            minimal_path_list = l.copy()
        if d2 < minimal_path_2:
            minimal_path_2 = d2
            minimal_path_list_sd = l2.copy()
    return matrix, minimal_path_list, minimal_path, minimal_path_list_sd, minimal_path_2


def read_data():
    f = open("C:/Users/ioana/OneDrive/Documents/Facultate/Semestrul 4/Inteligenta "
             "artificiala/Laborator/Artificial-Intelligence-Lab2/hard.txt", "r")
    n = int(f.readline())
    matrix = []

    # reading the matrix
    for i in range(n):
        line = f.readline()
        matrix.append([int(x) for x in line.split(',')])
    source = int(f.readline())
    destination = int(f.readline())
    f.close()
    return n, matrix, source, destination


def write_data(matrix, minimal_path_list, minimal_path, minimal_path_list_sd, minimal_path_2):
    f = open("C:/Users/ioana/OneDrive/Documents/Facultate/Semestrul 4/Inteligenta "
             "artificiala/Laborator/Artificial-Intelligence-Lab2/out.txt", "w")

    # first solution
    f.write("%s\n" % len(matrix))
    f.writelines("%s," % minimal_path_list[i] for i in range(len(minimal_path_list) - 1))
    f.write("%s\n" % minimal_path_list[len(minimal_path_list) - 1])
    f.write("%s\n" % minimal_path)

    # second solution
    f.write("%s\n" % len(minimal_path_list_sd))
    f.writelines("%s," % minimal_path_list_sd[i] for i in range(len(minimal_path_list_sd) - 1))
    f.write("%s\n" % minimal_path_list_sd[len(minimal_path_list_sd) - 1])
    f.write("%s\n" % minimal_path_2)
    f.close()


def main():
    data = read_data()
    n = data[0]
    matrix = data[1]
    source = data[2]
    destination = data[3]
    matrix, minimal_path_list, minimal_path, minimal_path_list_sd, minimal_path_2 = solve(matrix, source, destination)
    write_data(matrix, minimal_path_list, minimal_path, minimal_path_list_sd, minimal_path_2)


main()
