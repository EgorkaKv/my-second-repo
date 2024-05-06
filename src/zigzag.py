class ZigZag:
    def __init__(self, matrica, n, m):
        self.matrica = matrica
        self.n = n
        self.m = m
        self.zigzag_r = self.zig_route(self.matrica, self.n, self.m)

    def zig_route(self, matrix, n, m):
        zigzag = []
        kierunek = 0
        if n >= m:
            for i in matrix[m - 1][::-1]:
                temp = []
                y = m - 1
                x = matrix[y].index(i)

                while y > -1 and x < n:
                    temp.append(matrix[y][x])
                    y -= 1
                    x += 1

                if kierunek % 2 == 0:
                    temp.reverse()
                zigzag.extend(temp)
                kierunek += 1
            current_row = matrix[0][:m - 1]
            for i in current_row[::-1]:
                temp = []
                y = 0
                x = matrix[y].index(i)

                while x > -1 and y < m:
                    temp.append(matrix[y][x])
                    y += 1
                    x -= 1

                if kierunek % 2 != 0:
                    temp.reverse()
                zigzag.extend(temp)
                kierunek += 1

        else:
            for i in matrix:
                temp = []
                x = n - 1
                y = matrix.index(i)

                while x > -1 and y > -1:
                    temp.append(matrix[y][x])
                    y -= 1
                    x -= 1

                if kierunek % 2 == 0:
                    temp.reverse()
                zigzag.extend(temp)
                kierunek += 1

            for i in matrix[:n]:
                temp = []
                x = 0
                y = matrix.index(i)

                while x < n:
                    temp.append(matrix[y][x])
                    y -= 1
                    x += 1

                if kierunek % 2 != 0:
                    temp.reverse()
                zigzag.extend(temp)
                kierunek += 1
        return zigzag


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrica = []
    for i in range(m):
        List = list(map(int, input().split()))
        matrica.append(List)

    start = ZigZag(matrica, n, m)
    print(start.zigzag)
