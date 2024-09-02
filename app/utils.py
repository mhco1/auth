import re
from os import popen


def cmd(app ,c):
    res = None
    with app.suspend():
        cc = '$(pwd)/app/cmd.sh ' + str(c)
        res = popen(cc).read()
    return res

def convertJsonToTree(tree, jsonTree):
    jsonTree1 = jsonTree[0]
    tree1 = tree.root

    def recursive(t, j):
        if j['type'] == 'directory':
            tt = t.add(j['name'])

        if 'contents' in j.keys():
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
    res = []

    def recursive(node):
        if(node == None):
            res.reverse()
            return {
                'root': res[0],
                'path': res[1:],
            }
        txt = node.label.plain
        res.append(txt)
        return recursive(node.parent)
    
    return recursive(node)