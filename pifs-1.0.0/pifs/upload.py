import sys, os
from .encrypt import usecmd, encryptFs
from .ipfsApi import ipfsFileFunction


def ipfsUpload(filename):
    try:
        hash = []
        encryptFs(filename)
        for i in range(1,31):
            fn1 = filename + "-%s" % (i)
            ipfsFileFunction(fn1)
            h = ipfsFileFunction(fn1)
            hash.append(h)
            os.remove(fn1)
        with open(os.path.join("./KeyHash/",(filename + '-hash.txt')), 'w') as f:
            for item in hash:
                f.write("%s\n" % item)
        print("Upload successes")
    except:
        for i in range(1,31):
            fn1 = filename + "-%s" % (i)
            os.remove(fn1)
        print("Fail to Upload")

def run():
    filename = usecmd()
    ipfsUpload(filename)