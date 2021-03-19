H, M = map(int, input().split())

change_minute = 45
hour_minute = 60
hour = 24

if M - change_minute < 0:
    if H - 1 < 0:
        H = hour
    H -= 1
    M += hour_minute
M -= change_minute
print(H, M)
