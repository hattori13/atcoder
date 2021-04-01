# https://atcoder.jp/contests/abs/tasks/abc083_b

def main():
  n, a, b = map(int, input().split())

  # 1以上N以下の整数のうち、10進法での各桁の和がA以上B以下であるものの総和を出力する

  # 各桁の和を取得
  total = 0
  for num in range(1, n + 1):
    d_sum = digit_sum(num)
    # 範囲内なら元の値を加算
    if a <= d_sum and b >= d_sum:
      total += num
  
  print(total)

# 各桁の和
def digit_sum(n: int):
  nums = list(str(n))
  total = 0
  for num in nums:
    total += int(num)
  return total

# メイン処理
main()