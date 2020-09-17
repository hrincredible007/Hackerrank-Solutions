if __name__ == '__main__':
    lt=[]
    ltt=[]
    st=[]
    k=[]
    for i in range(int(input())):
        name = input()
        st.append(name)
        score = float(input())
        lt.append(score)
        maxx=99999999
        smax=99999999
        for i in range(len(lt)):
            if(lt[i]<maxx):
                smax=maxx
                maxx=lt[i]
            elif(lt[i]<smax and lt[i]!=maxx):
                smax=lt[i]
    for i in range(len(lt)):
        if smax==lt[i]:
            ltt.append(i)
    for i in ltt:
        k.append(st[i])
    for i in range(len(k)-1):
        for j in range(i+1,len(k)):
            if(k[i]>k[j]):
                k[i],k[j]=k[j],k[i]
    for i in k:
        print(i)
            
    
