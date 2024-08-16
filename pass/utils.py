import re
from os import popen


def cmd(app ,c):
    res = None
    with app.suspend():
        cc = '$(pwd)/pass/pass.sh ' + str(c)
        res = popen(cc).read()
    return res

def convertJsonToTree(tree, jsonTree):
    jsonTree1 = jsonTree[0]
    tree1 = tree.root

    def recursive(t, j):
        if j['type'] == 'directory':
            tt = t.add(j['name'])

            for jj in j['contents']:
                recursive(tt, jj)

        if j['type'] == 'file':
            t.add_leaf(re.sub(r'.gpg', '', j['name']))

        return
    
    if 'contents' in jsonTree1.keys():
        for x in jsonTree1['contents']:
            recursive(tree1, x)

    return

def getPathTree(node):
    def recursive(node, txt):
        txt1 = node.label.plain
        if(txt1 == 'password-store'): return txt[slice(-1)]
        txt = f"{txt1}/{txt}"
        return recursive(node.parent, txt)
    
    return recursive(node, '')