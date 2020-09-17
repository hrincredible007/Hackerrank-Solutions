def print_formatted(n)
    p=1
    r=bin(n)[2]
    l=len(r)
    for i in range(1,n+1)
        d=str(i)
        o=str(oct(i))[2]
        h=str(hex(i))[2].upper()
        b=str(bin(i))[2]
        print(%s %s %s %s % (d.rjust(l),o.rjust(l),h.rjust(l),b.rjust(l)))
        #print(%s %s %s %s % d.rjust(2),o.rjust(2), h.rjust(2), b.rjust(2))

