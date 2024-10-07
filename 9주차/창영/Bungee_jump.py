import sys
input = sys.stdin.readline

n = int(input().strip())

def n_down_up(max_n, n, down_up):
    print(n, end=' ')
    
    if n == max_n and down_up == 'up':
        return
    
    if n >= 1 and down_up == 'down':
        return n_down_up(max_n, n - 1, 'down')
    elif n == 0:
        return n_down_up(max_n, n + 1, 'up')
    else:
        return n_down_up(max_n, n + 1, 'up')

n_down_up(n, n, 'down')