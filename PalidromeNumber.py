#!/usr/bin/env python

def checkPalidrome(n):
        result=0
        number=str(n)
        x=len(number)
        for i in range(x/2):
                if(number[i] == number[x-i-1]):
                        result=1
                else:
                        reslut=0
        return result

 
x = int(input())
for i in range(x):
        inA,inB=raw_input().split();
        a=int(inA)
        b=int(inB)
        count=0;
        for n in range(a,b+1):
                r=checkPalidrome(n);
                if(r==1):
                        count+=1
        print(count)  


