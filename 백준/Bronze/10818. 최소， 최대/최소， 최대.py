import sys

n = int(input())

data = list(map(int,sys.stdin.readline().split()))

print(f"{min(data)} {max(data)}")