# https://atcoder.jp/contests/abs/tasks/abc081_a

input_data = str(input())

count = 0
for d in input_data:
  count += 1 if d == "1" else 0

print(count)

