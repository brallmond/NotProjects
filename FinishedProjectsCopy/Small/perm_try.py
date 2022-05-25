import itertools as itt

a = ['bing ', 'bang ', 'bonk ']
b = list(itt.combinations(a,2))
c = list(itt.combinations(a,3))

def put_together(perms):
  out_array = []
  for i in range(len(perms)):
    elem = ''
    j = 0
    while j<(len(perms[0])):
      elem += perms[i][j]
      j+=1
    out_array.append(elem)
  return out_array

a.extend(put_together(b))
a.extend(put_together(c))
print(a)
