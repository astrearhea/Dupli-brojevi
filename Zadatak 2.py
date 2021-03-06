from random import randrange
niz = []
for i in range(0,20):                                 #Potrebno je kreirati niz od 20 brojeva
    niz.append(randrange(0,100,3))                        #Računar bira random brojeva u rasponu od 0 do 100
print("Niz kreiran od strane računara:",niz)

niz2 = list(dict.fromkeys(niz))                       #Na ovaj način ćemo izbaciti duple brojeve
print("Niz nakon izbačenih duplih brojeva:",niz2)
print("Sada je broj članova niza:",len(niz2))

def mojMax(niz2):                                     #Prvi način određivanja maximalnog člana
    max = niz2[0]
    for x in niz2:
        if x > max:
            max = x
    return max
print("(I način)Maximalan član niza je:", mojMax(niz2))

print("(II način)Maximalan član niza je:", max(niz2))    #Drugi način određivanja maximalnog člana, preko već ugrađene funkcije

niz2.sort()
print("(III način)Maximalan član niza je:", niz2[-1])    #Treći način određivanja maximalnog člana, tako što se lista sortira rastući (od najmanjeg ka najvećem
# i pristupanje posljenjem(najvećem) članu


import heapq                                             #Četvrti, dodatni način određivanja maximalnog člana
y = heapq.nlargest(1,niz2)
print("(IV način)Maximalan clan niza je",y)