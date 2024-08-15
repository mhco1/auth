from os import popen


def cmd(app ,c):
    res = None
    with app.suspend():
        cc = '$(pwd)/otp/otp.sh ' + str(c)
        res = popen(cc).read()
    return res