def pythagorean_triplet(x):
    l=len(x)
    p=[]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                a=pow(x[i],2)+pow(x[j],2)
                b=pow(x[k],2)
                if(int(a)==int(b)):
                    q=[x[i],x[j],x[k]]
                    p.append(q)
    return p

llist=[1,5,2,8,9,3,4,9,6,10]
m=pythagorean_triplet(llist)
print(m)