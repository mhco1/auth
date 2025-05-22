import binascii
from textual.widgets import ListItem, Label

def convertToListView(txt='', op=[]):
    #txt = re.split(r'\\n', txt)
    txt = txt.encode().decode('unicode_escape')
    res = []

    for i in txt.strip().splitlines():
        arr = i.split(": ")
        #arr.append({"name": name, "id": id_})
        item = ListItem(Label(f'>{arr[0]}'), name=arr[0])
        item.prop = {}
        arr.pop(0)

        n = 0
        for ii in op:
            item.prop[ii] = arr[n]
            n += 1
        
        res.append(item)
    return res

def serialize(t=''):
    return t.strip().encode('utf8').hex()

def unserialize(t=''):
    return binascii.unhexlify(t.strip()).decode('utf8')