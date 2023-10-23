# Задача 5
# Напишите функцию, которая заполняет матрицу (m, n) в шахматном порядке заданными числами a и b
 
def chess(m, n, a, b):
    matrix = []
    prev = a

    for i in range(m):
        row = []
        for j in range(n):
            row.append(prev)

            prev = a if prev == b else b
        
        matrix.append(row)
    
    return matrix

inputFile = open("input.txt", "r")

testCount = int(inputFile.readline())

inputFile.readline()
 
for i in range(testCount):
    print ("Тест {}:".format(i + 1))

    m, n = list(map(int, inputFile.readline().split(" ")))
    a, b = list(map(int, inputFile.readline().split(" ")))

    print("Исходные данные:")
    print("m = {}, n = {}".format(m, n))
    print("a = {}, b = {}".format(a, b))

    print("Шахматная матрица:")
    for row in chess(m, n, a, b):
        for item in row:
            print("{}".format(item), end=" ")
        print()

    print("--------------------------------------------------")

    inputFile.readline()

inputFile.close()