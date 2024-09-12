import os
import shutil
import re


maindir=r'C:\Users\k1-on\Desktop\project'
targetdir=r'C:\Users\k1-on\Desktop\creat preview proj'


foldernames=[]
jpgs=[]



#creats a list with names of projects' folders > filling foldernames[] with projects directories
for i in os.listdir(maindir):
	if i[0:3].isdigit() and not'template'in i.casefold() and not'archive timelogs' in i.casefold():
		foldernames.append(i)

#function to look for the images files inside each project directory

def finder(name):
	#build path of project name
	mypath= maindir+'\\'+name
	
	#get the delivery category name

	deliveryfound=False
	highfound=False

	for delivery in os.listdir(mypath):

		if 'delivery' in delivery.casefold():
			mypath+='\\'+delivery
			deliveryfound=True

	if deliveryfound==False:	
		print(f'no delivery in {mypath}')
		return	

	for high in os.listdir(mypath):
		if 'high' in high.casefold():
			mypath+='\\'+high
			highfound=True

	if highfound==False:	
		print(f'no HIGH in {mypath}')
		return	

	count=0
	stached=mypath
	indfiles=[]

	for jpg in os.listdir(mypath):
		#need to count the files, and make a loop
		if '.jpg' in jpg.casefold():
			indfiles.append(jpg)
			
	for indfile in indfiles:
		jpgs.append(mypath+'\\'+indfile)

	if len(indfiles)==0:
		print(f'no files in {mypath}')
		


#initiate the finder function to fill in jpgs array with directories of images:
for project in foldernames:
	finder(project)


#copy files in jpgs array to a new folder:

for imagefile in jpgs:
	
	newobj=shutil.copy2(imagefile,targetdir)
	myname=imagefile.split("\\")[-1]

	#to get file name
	titles=imagefile.partition(maindir+'\\')

	#to get project name
	projname =titles[2].split('\\')[0]
	
	os.rename(targetdir+'\\'+myname,targetdir+'\\'+projname.upper()+'_'+myname)


	#print ('successful copy of >> ',newobj)



############### to do list #######################

# 4- add control mechanism to make sure that it doesnt create duplicates each time the script is run... or optional range
