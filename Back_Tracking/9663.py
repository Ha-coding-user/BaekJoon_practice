from sys import stdin
input = stdin.readline

N = int(input())

col = [None] * N

def promising(cdx):
   
    for i in range(cdx):
        if  col[cdx] == col[i] or cdx - i == abs(col[cdx] - col[i]):
            return 0
        
    return 1

def nQueens(cdx):
    global count

    if cdx == N:
        count += 1
        return

    for i in range(N):
        col[cdx] = i
        if promising(cdx):
            nQueens(cdx+1)

count = 0
nQueens(0)

print(count)