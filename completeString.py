#!/usr/bin/env python
 
x = int(input())
for i in range(x):
	str=str(input())
	count=0
	for s in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
		if(s in str):
			count+=1
	if(count==26):
		print("YES")
	else:
		print("NO")