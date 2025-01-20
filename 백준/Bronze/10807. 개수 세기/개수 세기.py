import sys

a = int(input())

ls = list(map(int,sys.stdin.readline().split()))

find = int(input())

print(ls.count(find))
