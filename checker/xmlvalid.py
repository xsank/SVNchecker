'''
Created on 2013-10-8

@author: xsank
'''

from xml.dom import minidom

def run(file):
    msg=""
    exitCode=0
    
    if is_xmlfile(file):
        try:
            f=open(file,'r')
            minidom.parse(f)
        except Exception,e:
            msg="xml file:%s valid error:\n%s" % (file.split('/')[-1],e)
            exitCode=1
        finally:
            f.close()
    
    return (msg,exitCode)
    
def is_xmlfile(filename):
    files=filename.split('.')
    if len(files)==1:
        return False
    else:
        return files[-1]=='xml'
