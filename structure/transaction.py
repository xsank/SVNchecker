'''
Created on 2013-10-8

@author: xsank
'''
import os
import shutil
import tempfile

import process
from checker import jsonvalid
from checker import xmlvalid
from checker import logvalid

class Transaction:
    def __init__(self,repos,txn):
        self.repos=repos
        self.txn=str(txn)
        
        try:
            int(self.txn)
            self.type="revision"
        except ValueError:
            self.type="transaction"
        
        self.tmpdir=tempfile.mkdtemp()
        
    def __executeSVN(self,command,arg="",split=False):
        command="svnlook --%s %s %s %s %s" % (self.type,self.txn,command,self.repos,arg)
        output=process.execute(command)
        if split:
            output=[x.strip() for x in output.split("\n") if x.strip()]
            
        return output
    
    def get_file(self,filename):
        tmpfile=os.path.join(self.tmpdir,filename)
        if(os.path.exists(tmpfile)):
            return tmpfile
        
        content=self.__executeSVN("cat", "\""+filename+"\"")
        dirname=os.path.dirname(filename)
        tmpdir=os.path.join(self.tmpdir,dirname)
        if dirname and not os.path.exists(tmpdir):
            os.makedirs(tmpdir)
            
        fd=open(tmpfile,"w")
        fd.write(content)
        fd.flush()
        fd.close()
        
        return tmpfile
        
    
    def get_files(self):
        output=self.__executeSVN("changed", split=True)
        files={}
        for entry in output:
            attrs=entry[0:3].strip()
            filename=entry[4:].strip()
            files[filename]=attrs
        return files
    
    def get_user(self):
        user=self.__executeSVN("author")
        return user.strip()
    
    def get_cmtlog(self):
        output=self.__executeSVN("info",split=True)
        temp=output[3:]
        msg="".join(temp)
        return msg.strip()
    
    def cleanup(self):
        shutil.rmtree(self.tmpdir)
        
    def check(self):
        msg,exitCode=logvalid.run(self.get_cmtlog())
        if exitCode!=0:
            return (msg,exitCode)
        else:
            for file in self.get_files().keys():
                msg=jsonvalid.run(self.get_file(file))[0] or xmlvalid.run(self.get_file(file))[0]
                exitCode=jsonvalid.run(self.get_file(file))[1] or xmlvalid.run(self.get_file(file))[1]
                return (msg,exitCode)
    
        
        
