def intersection(a,b):
    ans=[]
    p=0
    while(p<len(a)):
      if a[p] in dic:
         start=p
         dis=float("-inf")
         for k in dic[a[p]]:
             index=p
             while(index<len(a) and k<len(b) and a[index]==b[k]):
                    index+=1
                    k+=1
             dis=max(index-start,dis)
         p=start+dis
         ans.append(a[start:start+dis])
      else:
         p+=1
    return ans
a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
intersection(a,b)