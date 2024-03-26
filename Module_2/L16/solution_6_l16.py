def create_workspace(size):
    workspace = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
                if i == size - j - 1 and i != j:
                    workspace[i][j] = 5
                elif i < j < size - i - 1 and i < size:
                    workspace[i][j] = 1
                elif size - i - 1 < j < i and i > size // 2:
                    workspace[i][j] = 3
                elif size + i + 1 > i > j and i < size - 1 // 2:
                    workspace[i][j] = 2
                elif i < j < size + i + 1 and i < size + 1 // 2:
                    workspace[i][j] = 4

    for row in workspace:
        print(*row)

size = 5
create_workspace(size)