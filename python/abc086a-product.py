# https://atcoder.jp/contests/abs/tasks/abc086_a

a,b = map(int, input().split())
# print("Odd" if (a * b) % 2 == 1 else "Even")

if (a * b) % 2 == 1:
  print("Odd")
else:
  print("Even")