'''
Created on 2013-10-8

@author: xsank
'''

import sys

from structure import transaction

def finish(msg,exitCode):
    if exitCode!=0:
        print msg
    sys.exit(exitCode)

if __name__=='__main__':
    repos=sys.argv[1]
    txn=sys.argv[2]
    
    trans=transaction.Transaction(repos,txn)
    msg,exitCode=trans.check()
    trans.cleanup()
    finish(msg,exitCode)
