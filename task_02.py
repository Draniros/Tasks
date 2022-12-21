def coincidence(ulist = [],urange = []):
    llist = []
    lrange = []
    if(ulist == [] or urange == []):
        return llist
    else:
        for n in urange:
            lrange.append(n)
        start = min(lrange)
        stop = max(lrange)+1
        for i in ulist:
            if(isinstance(i, (int, float))):
                if(i >= start and i < stop):
                    llist.append(i)
        llist.sort()
        return llist
    
lst = [5.65,7,7.2,9,4,2,20,8]
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
print(coincidence(lst,range(4,8)))
