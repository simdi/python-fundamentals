def hanoi(n, start, goal, ignore):
  if n == 1:
    print(start, '--->', goal)
    return

  hanoi(n-1, start, ignore, goal)
  print(start, '--->', goal)
  hanoi(n-1, ignore, goal, start)

hanoi(4, 1, 2, 3)

"""Output"""
# 1 ---> 3
# 1 ---> 2
# 3 ---> 2
# 1 ---> 3
# 2 ---> 1
# 2 ---> 3
# 1 ---> 3
# 1 ---> 2
# 3 ---> 2
# 3 ---> 1
# 2 ---> 1
# 3 ---> 2
# 1 ---> 3
# 1 ---> 2
# 3 ---> 2