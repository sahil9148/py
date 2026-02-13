l =[1,2,2,9,3,2]
for i in range(1,len(l)-1):
    if sum(l[0:i])==sum(l[i+1:len(l)]):
        print(i)
        break
