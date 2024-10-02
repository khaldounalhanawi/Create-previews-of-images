import os
path=r"C:\Users\k1-on\Documents"


def findjpgs (mypath):
	alljpgs=[]

	try:
		folders=os.listdir(mypath)
	except:
		return(alljpgs)

	mappedcontents=map(lambda x:mypath+'\\'+x,folders)

	for content in mappedcontents:
		if content[-4:]=='.jpg':
			alljpgs.append(content)
		else:
			alljpgs+=findjpgs(content)
	
	return(alljpgs)




print(*findjpgs(path),sep='\n')	

