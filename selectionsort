#!/usr/bin/env python

#selection sort


def selection_sort(a,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(a[j]>a[min]):
                min=j
        t=a[i]
        a[i]=a[min]
        a[min]=t
    return a


tc=input();
for i in range(tc):
    l=input()
    tmp=list(map(int, raw_input().strip().split(" ")))
    result=selection_sort(tmp,l)
    for x in result:
        print x,
    print ""



        

        
