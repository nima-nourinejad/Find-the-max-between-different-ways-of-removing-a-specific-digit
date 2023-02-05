def index(a,b):
  list_a=[]
  a=str(a)
  b=str(b)
  index_b=[]
  for i in a:
    list_a.append(i)
  n=list_a.count(b)
  if n==0:
    index_b='NAN'
  else:
    for i in range (n):
      index_b.append(int((list_a.index(b)))+i)
      list_a.pop(list_a.index(b))
  return index_b

def poped_index (c,d):

  list_c=[]
  poped=''
  poped_list=[]
  out=[]
  c=str(c)
  d=str(d)
  if index(c,d)=='NAN':
    out.append (int(c))
  else:
   for i in index(c,d):
     for j in c:
       list_c.append(j)
     list_c.pop (i)
     for k in list_c:
       poped=poped+k
     poped_list.append(int(poped))
     poped=''
     list_c=[]
   out=poped_list
  return out
def maxx (e):
  j=0
  a=0
  for i in e:
    if j==0:
      a=i
      j=1
    elif j==1:
      if i>a:
        a=i
      else:
        pass
  return a
def nahaiat (f,g):
  return (maxx (poped_index (f,g)))
