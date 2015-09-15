
#merge two sorted arrays

def mergeSortedArrays(a,b,n,m):
    k=0,i=0j=0
    while(i<n and j<m):
        if(a[i] >= b[j]):
            result[k++]=a[i++]
        else:
            reslut[k++]=b[j++]
    if(i<n):
        for p in range(i,n):
            result[k++]=a[p]
    else:
        for p in range(i,m):
            result[k++]=b[p]

tc=input();
for i in range(tc):
     inA,inB=raw_input().split();
     n=int(inA)
     m=int(inB)
     arr1=list(map(int, raw_input().strip().split(" ")))
     arr2=list(map(int, raw_input().strip().split(" ")))

     result=merge(arr1,arr2,n,m)
     for x in result:
        print x,
    print ""
     
