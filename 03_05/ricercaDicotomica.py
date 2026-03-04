#retituisce true se l'elemento cercato è nella lista, altrimenti False
 
def ricercaDicotomica(l,n):
    i = 0
    f = len(l)-1
    while i<=f:            
        m = (i+f)//2
        if l[m] == n:
            return True
        if l[m] > n:
            f = m - 1
        elif l[m] < n:
            i = m + 1
    return False
 
lista = [10,12,44,72,88,96,104,1000]
print(ricercaDicotomica(lista,100))