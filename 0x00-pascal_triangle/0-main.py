#!/usr/bin/python3

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def pascal_triangle(n):
    if n <= 0:
        return []


    triangle = [[1]]
    for i in range(1, i):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)

            return triangle
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
            if __name__ == "__main__":
                print(pascal_triangle(5))
