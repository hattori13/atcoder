# https://atcoder.jp/contests/abs/tasks/abc081_b

size = input()
input_data = list(map(int, input().split()))
l_si = [int(s) for s in input_data]

print(l_si)

l_si_next = l_si
is_next = True
count = 0
while(True):
  l_si_temp = []
  for si in l_si_next:
    si_harf = si / 2
    l_si_temp.append(si_harf)
    if si_harf % 2 == 1:
      is_next = False
      break
  
  if not is_next:
    break
  else:
    l_si_next = l_si_temp
    count += 1

print(count)