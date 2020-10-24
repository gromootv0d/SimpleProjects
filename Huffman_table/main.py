# def work(a):
#     for row in reversed(1, range(len(a))):
#         for elem in range(len(a[row])):
#             print(a[row][elem], end=' ')
#         print()
#
# def reversed_print(a):
#     for row in reversed(range(len(a))):
#         for elem in range(len(a[row])):
#             print(a[row][elem], end=' ')
#         print()
#
# def printM(a):
#     for row in a:
#         for elem in row:
#             print(elem, end=' ')
#         print()
# mas = [0.158,
# 0.0945,
# 0.0756,
# 0.0722,
# 0.0636,
# 0.0584,
# 0.0430,
# 0.0430,
# 0.0344,
# 0.0344,
# 0.0326,
# 0.0326,
# 0.0309,
# 0.0275,
# 0.0258,
# 0.0241,
# 0.0241,
# 0.0206,
# 0.0189,
# 0.0189,
# 0.0172,
# 0.0137,
# 0.0086,
# 0.0069,
# 0.0069,
# 0.0052,
# 0.0052,
# 0.0017,
# 0.0017]
# mas = [6,5,4,3,2,1]
# n = len(mas)
# m = n * 2
# a = [0] * n
#
# for i in range(n):
#     a[i] = [0] * m
# sum = 0
# for i in range(n):
#     a[i][0] = mas[i]
#     sum+=mas[i]
#
# printM(a)
# print(sum)
# reversed_print(a)




# print()
#
# for i in range(1,m):
#     for j in range(n):
#         if (i+1)%2 == 0:
#             mas[j][i] = mas[j][i-1]

class Huffman:
    def __init__(self):
        """constructor"""
    def start(self):
        self.make_arr()
        self.hauffman_work()
        self.pring()
        print('-' * 100)

    def another_print(self):
        pass

    def pring(self):
        # for i in self.mas:
        #     for j in i:
        #         print(j, end= " ")
        #     print()
        max_len = max([len(str(e)) for r in self.mas for e in r])
        for row in self.mas:
            print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))
    def make_arr(self, k = 6):

        input = [0.1578,
0.0945,
0.0756,
0.0722,
0.0636,
0.0584,
0.0430,
0.0430,
0.0344,
0.0344,
0.0326,
0.0326,
0.0309,
0.0275,
0.0258,
0.0241,
0.0241,
0.0206,
0.0189,
0.0189,
0.0172,
0.0137,
0.0086,
0.0069,
0.0069,
0.0052,
0.0052,
0.0017,
0.0017]
        input = [0.5, 0.15, 0.15, 0.1, 0.05, 0.05]
        k = len(input)
        self.n = k
        self.m = self.n * 2
        self.mas = [-1] * self.m
        for i in range(self.m):
            self.mas[i] = [-1] * self.n
        for i in range(self.n):
            self.mas[0][i] = input[i]
    def hauffman_work(self):
        m = self.m
        n = self.n
        mas = self.mas
        counter = 0
        for i in range(1,m):
            counter += 0.5
            for j in range(n):
                if (i + 1) % 2 == 0:
                    mas[i][j] = mas[i-1][j]
                else:
                    if j > counter:
                        mas[i][j] = mas[i - 1][j]
                    elif j == counter:
                        mas[i][j] = round(mas[i-1][j] + mas[i-1][j-1], 4)
                        #mas[i][j] = (mas[i-1][j] + mas[i-1][j-1])
                    else:
                        mas[i][j] = 0
            if (i + 1)% 2==0:
                mas[i].sort()

if __name__ == "__main__":
    hauffman = Huffman()
    hauffman.start()



