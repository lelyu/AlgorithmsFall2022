#@author: Le Lyu, lyule@bc.edu. @credit: Syed Ramin
from lib2to3.pgen2.pgen import ParserGenerator
import random
from textwrap import indent


def parse(str):
    indices = []
    values = []
    for c in str.split():
        if len(indices) < 1:
            indices = c.replace("(", "").replace(")", "").split(",")
        else:
            values = c.replace("(", "").replace(")", "").split(",")
    return [indices, values]


def SAT():
        
    f = open("3SAT.txt", "r")
    # there are 80 lines in f
    biglist = []
    for line in f:
        p = parse(line)
    # example of p: [['6', '5', '13'], ['1', '1', '0']]. p[0] is the index, p[1] is the constraint
        indices = p[0]
        indices = list(map(int, indices))
        constraints = p[1]
        constraints = list(map(int, constraints))
        biglist.append([indices, constraints])




    sum = 0
    for i in range(20):
        Z = 0
        a = []
        for i in range(20):
            a.append(random.randint(0, 1))

        for i in biglist:
            count = 0
            for j in range(3):
                # print(i[0][j])
                # print(a[i[0][j]-1])
                if a[i[0][j]-1] == i[1][j]:
                    count += 1
            if count == 3:
                Z += 1
        sum += Z
    return sum/20



sum = 0
for i in range(20):
    sum += SAT()

print(sum/20)