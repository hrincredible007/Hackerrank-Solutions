def minion_game(s):
    k=kk=0#Banana
    for i in range(len(s)):
        if(s[i] in "AEIOU"):
            k+=len(s)-i
        else:
            kk+=len(s)-i#6 4  
    if(k>kk):
        print("Kevin",end=" ")
        print(k)
    elif(k<kk):
        print("Stuart",end=" ")
        print(kk)
    else:
        print("Draw")