import os

folderpath=r'C:\Users\k1-on\Documents\Python World\create previews'
report=''




def finder(path,report):
	projects=[]
	deliverys=[]
	high=[]
	jpgs=[]
	report=''

	for i in os.listdir(path):
		if i[:3].isdigit() and not '.' in i:
			projects.append(i)

	projectspaths=[a+'\\'+b for a, b in zip([path]*len(projects), projects)]

	def target (mypath,keyword,mytargetlist,rr):
		contents=os.listdir(mypath)
		if len(contents)==0:
			rr+= f'No {keyword} in {mypath}\n'
		else:
			keywordcount=0
			for files in contents:
				
				if keyword in files.casefold():
					mytargetlist.append(mypath+'\\'+files)
					keywordcount+=1
			if keywordcount==0:
				rr+= f'No {keyword} in {mypath}\n'	

			
		return rr, mytargetlist

	for i in projectspaths:
		report,deliverys=target(i,'delivery',deliverys,report)
	for i in deliverys:
		report,high=target(i,'high',high,report)
	for i in high:
		report,jpgs=target(i,'.jpg',jpgs,report)

	
	return(jpgs,report)



finalpath,report=finder(folderpath,report)

print (*finalpath, sep='\n') 
print(report)
