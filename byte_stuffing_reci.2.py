f=open("byte.txt","r")
s1=f.readlines()
f.close()
s2=''
l=len(s1)
i=0
while i<l:
	j=0
	while j<len(s1[i]):
		if(s1[i][j]=='/'):
			s2=s2+s1[i][j+1]
			j=j+2
		elif s1[i][j]=='#':
			s2=s2+' '
			j=j+1
		else:
			s2=s2+s1[i][j]
			j=j+1
	i=i+1

print s2
f=open("byte","w")
f.write(s2)

        
    
