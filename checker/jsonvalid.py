'''
Created on 2013-10-8

@author: xsank
'''
import simplejson as json

def run(file):
    msg=""
    exitCode=0
    
    if is_jsonfile(file):
        try:
            f=open(file,'r')
            content="".join(f.readlines())
            #content=content.strip("'<>[](){}\"` ").replace('\'','\"')
            jsonobj=json.loads(content,strict=False,encoding="UTF-8")
        except Exception,e:
            msg="json file:%s valid error:\n%s" % (file.split('/')[-1],e)
            exitCode=1
        finally:
            f.close()
    
    return (msg,exitCode)
    
def is_jsonfile(filename):
    files=filename.split('.')
    if len(files)==1:
        return False
    else:
        return files[-1]=='json'
    
