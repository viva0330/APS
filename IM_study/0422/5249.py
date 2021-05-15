import sys
sys.stdin = open('5249_sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    n1, n2, w = map(int, input().split())