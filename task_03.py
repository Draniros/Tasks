def max_odd(array):

    i = len(array)-1 
    maxs = 0

    while i != -1:
        if(isinstance((array[i]),int|float)):
            per = int(array[i])
            if(per%2 == 1):
                if(per > maxs): maxs = per
        i-=1

    if(maxs == 0):
        return "None"
    else:
        return maxs

print(max_odd([7, 'ololol', None, 9.00, 3, 22]))
print(max_odd(['ololol', 2,4]))
print(max_odd([1, 2, 3, 4, 4]))
print(max_odd(['ololo', 'fufufu'])
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])
