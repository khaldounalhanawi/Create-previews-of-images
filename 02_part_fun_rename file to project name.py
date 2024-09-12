#creates a new path for a given path, which will have the name of the file modified to inclube the name of the project
#############


txt=r'R:\01_renderkitchen\01_projekte\782 Paco\08 Delivery\HIGH\240425_Paco_Halle_Kam_Seitlich_HIGH.jpg'

import re

def attachprojectname(txt):
    #get file name
    pattern=r'[^\\]+$'
    filename=re.findall(pattern,txt)

    #get project name
    patternproj=r'projekte\\([^\\]+[^\\])'
    projectname=re.findall(patternproj,txt)

    #get path of file without the file's name
    stxt= txt.split('\\')
    stxt.pop(-1)
    path='\\'.join(stxt)

    #prints the new path
    print(path+'\\'+projectname[0]+'_'+filename[0])

    
#initiate the function    
attachprojectname(txt)

