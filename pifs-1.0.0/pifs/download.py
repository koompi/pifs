import sys, os
import subprocess
from .decrypt import usecmd, decryptFs
from .ipfsApi import ipfsFileget



def ipfsDownload(filename, key):
    try:  
        fn1 = filename + "-hash.txt"
        hash = [line.rstrip('\n') for line in open(os.path.join('./KeyHash/',fn1))]
        for i in hash:
            ipfsFileget(i)
        decryptFs(filename,hash, key)
        print("Download successes")
    except:
        print("Download fail")

def run():
    filename, key = usecmd()
    ipfsDownload(filename, key)

