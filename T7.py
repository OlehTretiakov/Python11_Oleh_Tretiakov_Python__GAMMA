time = int(input())
s_d = 24 * 60 * 60
d = time // s_d
h = time % s_d // 3600
m = time % s_d % 3600 // 60
s = time % 60
print(f"{d}:{h}:{m}:{s}")