def sum_f(l):
     number = 0
     for num in l:
         number += num
     return number



def sum_w(L):
     number = 0
     while len(l) > 0:
         number += l[-1]
         L.pop()
     return number



def sum_r(L, n=0):
      if  len(l) == 0:
          return n
      return sum_r(l[1:], l[1]+n)



