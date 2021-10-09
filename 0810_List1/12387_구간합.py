import sys
sys.stdin = open('12387.txt', 'r')

T = int(input())
for tc in range(T):
   N,M = map(int,input().split())
   numbers = list(map(int, input().split()))

   number_list = []
   for i in range(1, N):

       for j in range(0, N-2):
           max = number_list[0]
           if max < number_list[j]:
               max = number_list[j]

           min = number_list[0]
           if min > number_list[j]:
               min = number_list[j]
       print(max, min)

