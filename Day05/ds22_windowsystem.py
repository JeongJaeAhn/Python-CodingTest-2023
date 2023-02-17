# C:\Windows\System32 파일 출력
import os

#print(dir(os))
def makeFileList(folder):
    fnameAry = []
    for _, _, fnames in os.walk(folder):
        for fname in fnames:
            fnameAry.append(fname)

    return fnameAry
    
def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if ary[cur-1] < ary[cur]:   # 내림차순(역순정렬)
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]

    return ary

fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print('파일명 역순 -->', fileAry)