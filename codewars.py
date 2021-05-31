def next_bigger(n):
    x = [int(i) for i in str(n)]
    temp = ""
    alln = []
    while True:
        swapped = 0
        for i in range(0, len(x)-1):
            currentnr = ""
            temp = x[i]
            x[i] = x[i+1]
            x[i+1] = temp
            for p in x:
                currentnr = currentnr + str(p)
            if not int(currentnr) in alln:
                alln.append(int(currentnr))
                swapped = 1
        if swapped == 0:
            break
    salln = bsort(alln)
    for i in range(0, len(salln)):
        if salln[i] == n:
            return salln[i+1]
    
            
        
def bsort(l):
    temp = 0
    while True:
        swapped = 0
        for i in range(0, len(l)-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                swapped = 1
        if swapped == 0:
            break            
    return l


print(next_bigger(4809))