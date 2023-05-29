def two_sum_hashed(l, target):
    d={}
    d2={}
    for i in range(0,len(l)):
        d[i]=l[i]
    for key , value in d.items():
        d2[value]=key
    del d
    lst=[]
    for key, value in d2.items():
        diff=target-key
        if diff in d2.keys():
            lst.append([value, d2.get(diff)])
    for item in lst:
        reversed_iterator=list(reversed(item))
        if reversed_iterator in lst and item!=reversed_iterator:
            lst.remove(item)
    lst=[tuple(i) for i in lst]
    return(lst)

assert two_sum_hashed([1, 5, 3, 8, 4, 2], 6)==[(1, 0), (2, 2), (5, 4)]
