if __name__ == '__main__':
    n = int(input())
    lt = map(int, input().split())
    lt=list(set(list(lt)))
    maxx=-9999999
    smax=-9999999
    for i in range(len(lt)):
        if(maxx<lt[i]):
            smax=maxx
            maxx=lt[i]
        elif(maxx!=lt[i] and lt[i]>smax):
            smax=lt[i]
    print(smax)