def generate_spiral_matrix(width):
    matrix = [[0 for _ in range(width)] for _ in range(width)]
    num = 1
    top, bottom, left, right = 0, width - 1, 0, width - 1

    while num <= width * width:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    max_length = len(str(width * width))
    for row in matrix:
        print(" ".join(str(cell).rjust(max_length) for cell in row))

width = 4
generate_spiral_matrix(width)