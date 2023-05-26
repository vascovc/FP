import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)

printDirFiles("..")


def findFiles(d, ext):
    lst = os.listdir(d)
    lst_1 = []
    exten = len(ext)
    for fname in lst:
        path = os.path.join(d,fname)
        if os.path.isfile(path):
            if str(fname[-exten:]) == ext:
                lst_1.append(fname)
        elif os.path.isdir(path):
            lst_1.append(findFiles(path,ext))            
    return lst_1


# Test findFiles:
lst = findFiles(".", ".py")
print(lst)
assert isinstance(lst, list)

lst = findFiles("..", ".csv")
print(lst)

