import os
import shutil
import re
from PIL import Image

maindir=r'R:\01_renderkitchen\01_projekte'
targetdir=r'C:\Users\Khaldoun\Desktop\preview'


foldernames=[]
jpgs=[]

def resizeimage(imagefile):
    im = Image.open(imagefile)
    aspect = im.size[0] / im.size[1]

    width = 1000
    height = int(width / aspect)  # Cast to int since resize expects integer dimensions
    
    # Resize the image
    resized_im = im.resize((width, height))
    
    # save the resized image
    resized_im.save(imagefile)
    
    print('image resized')

#creats a list with names of projects' folders > filling foldernames[] with projects directories
for i in os.listdir(maindir):
	if i[0:3].isdigit() and not'template'in i.casefold() and not'archive timelogs' in i.casefold() and not '.' in i.casefold():
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
	jaja=0
	for high in os.listdir(mypath):
		if 'high' in high.casefold():
			jaja+=1
			if jaja==1:
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
	

	titles=imagefile.partition(maindir+'\\')
	myname=imagefile.split("\\")[-1]
	#to get project name
	projname =titles[2].split('\\')[0]
	newname=targetdir+'\\'+projname.upper()+'_'+myname
	#print (newname)
	checklist=os.listdir(targetdir)
	checkname=projname.upper()+'_'+myname
	#print()
	if checkname in checklist:
		#print(f'file already exists> {checkname}')
		continue


	

	newobj=shutil.copy2(imagefile,targetdir)
	

	#to get file name
	

	os.rename(targetdir+'\\'+myname,newname)
	imagefile=newname
	try:
		resizeimage(imagefile)
	except:
		print(f'Image too large> {imagefile}')	

	#print ('successful copy of >> ',newobj)




############### to do list #######################

# Multiple high folders problem


