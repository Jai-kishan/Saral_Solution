a=[23,54,67,54,12,43,65,47,89,54]
i=0
b=0
while i<len(a):
	j=i+1
	while j<len(a):
		if a[i]>a[j]:
			b=a[i]
			a[i]=a[j]
			a[j]=b
		j+=1
	print(a[i])
	i+=1