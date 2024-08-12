import gnupg

gpg = gnupg.GPG(gnupghome='/home/x/.gnupg')
res = gnupg.Verify(gpg)
print('ok')