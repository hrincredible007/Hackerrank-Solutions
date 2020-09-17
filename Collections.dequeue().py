n=int(input())
for i in range(n):
    s=input()
    k=s.split()
    if(len(k)==2):
        if(k[0]=="append"):
            deque.append(int(k[1]))
        if(k[0]=="appendleft"):
            deque.insert(0,int(k[1]))
    else:
        if(k[0]=="pop"):
            deque.pop()
        else:
            deque.pop(0)
for i in deque: 
    print(i,end=" ")
