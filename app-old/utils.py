import re
import binascii
from textual.widgets import Input

# def Input1(*a,**b):
#     i = Input(*a,**b)
#     #i.styles.height = 1
#     #i.styles.border = ('none','red')
#     #i.styles.background = '#1e90ff'
#     return i

def convertJsonToTree(name, tree, jsonTree):
    jsonTree1 = jsonTree[0]
    tree.reset(name)
    tree1 = tree.root
    #tree1.reset(name)

    def recursive(t, j):
        if re.search(r'.key$', j['name']):
            return t.add_leaf(re.sub(r'.key$', '', j['name']))
        
        tt = t.add(j['name'])

        if 'contents' in j.keys():
            for jj in j['contents']:
                recursive(tt, jj)

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
            return res
        txt = node.label.plain
        res.append(txt)
        return recursive(node.parent)
    
    return recursive(node)

def serialize(t=''):
    return t.encode('utf8').hex()

def unserialize(t=''):
    return binascii.unhexlify(t).decode('utf8')