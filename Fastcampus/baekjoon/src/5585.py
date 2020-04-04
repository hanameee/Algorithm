changes = 1000 - int(input())
count = 0

for coin in [500, 100, 50, 10, 5, 1]:
  	count += changes // i  # 몫
    changes %= i # 나머지

print(count)
