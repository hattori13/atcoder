# https://atcoder.jp/contests/abs/tasks/abc081_b

def main():
  size = input()
  input_data = list(map(int, input().split()))
  list_data = [int(item) for item in input_data]

  shift_count = 0
  list_data_next:list = list_data
  is_next = True
  while(is_next):
    is_next = is_shiftable(list_data_next)
    if is_next:
      shift_count += 1
      list_data_next = shift_items(list_data_next)

  print(shift_count)

# 引数のリストの要素が全てシフト可能か判定する
def is_shiftable(list: list) -> bool:
  for item in list:
    if item % 2 == 1:
      return False
  return True

# 引数のリストの要素を右シフトする
def shift_items(list: list) -> list:
  list_temp = []
  for item in list:
    shifted = item >> 1
    list_temp.append(shifted)
  return list_temp

# main関数の実行
main()
