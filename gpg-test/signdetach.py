import os
import fs
from fs import open_fs
import gnupg

gnupghome = '/home/x/.gnupg'
#fs1 = open_fs(".")
files_dir = []

gpg = gnupg.GPG(gnupghome)

if os.path.exists("./signatures/"):
        print("Signatures directory already created")
else:
        fs.makedir(u"./signatures")
        print("Created signatures directory")

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    files_dir.append(f)