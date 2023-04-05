def splitevodd(a):
    evenlist=[]
    oddlist=[]
    for i in a:
        if(i % 2== 0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("even lists:",evenlist)
    print("odd lists:",oddlist)
    
#drive code
a=list()
n=int(input("enter the size of the first list ::"))
print("enter the element on first list::")
for i in range(int(n)):
      k=int(input(""))
      a.append(k)
      splitevodd(a)  
