import sys
sys.stdin = open('pg.txt', 'r')

def solution(mylist):
    mylist = list(map(len, mylist))
    return mylist

mylist = list(input().split())
solution(mylist)
