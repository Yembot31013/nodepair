from array import array


def errorFind(arr):
  r = []
  a = []
  for e, i in enumerate(arr):
    if i in a:
      if a[-1] > i:
        r.append(i)
        r.append(a[-1]+1)
      if a[-1] == i:
        r.append(i)
        r.append(a[-1]+1)
    else:
      a.append(i)
  print(r)
  print(a)

ins = input().split()
l = list(map(int, ins))
errorFind(l)