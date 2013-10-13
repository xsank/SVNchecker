'''
Created on 2013-10-8

@author: xsank
'''
MIN_LOG_LENTH=9

def run(content):
    msg=""
    exitCode=0
    if len(content)<MIN_LOG_LENTH:
        msg="your commit log is too short,please rewrite it again!"
        exitCode=1
    
    return (msg,exitCode)
