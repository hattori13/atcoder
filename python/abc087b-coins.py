# https://atcoder.jp/contests/abs/tasks/abc087_b

a = int(input())
b = int(input())
c = int(input())
x = int(input())

pattern_count = 0

for count_a in range(0, a + 1):
  total_a = 0
  total_a += count_a * 500
  for count_b in range(0, b + 1):
    total_ab = total_a
    total_ab += count_b * 100
    for count_c in range(0, c + 1):
      total_abc = total_ab
      total_abc += count_c * 50
      if total_abc == x:
        pattern_count += 1
      elif total_abc > x:
        break

print(pattern_count)
