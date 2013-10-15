'''
Created on 2013-10-9

@author: xsank
'''

import subprocess

class ProcessException(Exception):
    def __init__(self,command,exitCode,output):
        self.command=command
        self.output=output
        self.exitCode=exitCode
        
    def __str__(self):
        return "command %s exited with code %s:\n%s" % (self.command,self.exitCode,self.output)
    
def execute(command):
    process=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output=process.communicate()[0]
    exitCode=process.returncode
    
    if exitCode==0:
        return output
    else:
        raise ProcessException(command,exitCode,output)
