import random

def nimRandom(n):
  t = random.randrange(1, min(3, n) + 1)
  return t

def nimOptimal(n):
  t = n % 4
  if t == 0:
    t = nimRandom(n)
  return t

def nimHuman(n):
  # FIXME: need to check validity of move and ask again if not valid
  t - int(input('%d sticks left, type number to take: ' %n))
  return t

def simpleNimController(n, p1, p2):
  print('%d sticks left' %n)
  t = pl(n)
  n = n - t
  print('Player took %d, noe %d sticks left' % (t, n))
