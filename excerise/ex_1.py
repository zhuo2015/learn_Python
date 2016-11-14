import os
os.chdir('c:\\Users\\john\HFpython')

def sanitize(time_string):
    # 修改时间字段的格式，统一为‘min.sec’
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (min,sec) = time_string.split(splitter)
    return(min+'.'+sec)

def notrepeat(repeat):
    notre=[]
    for each in repeat:
        if each not in notre:
            notre.append(each)
    return notre


for i in os.listdir():
    # 从文件列表中，读取每一个文件，并生成列表
    c = open(i).readline().strip().split(',')
    # 转换文件内容为统一的时间格式
    #c1=[float(sanitize(each)) for each in c]
    #c2=sorted(notrepeat(c1))
    c2 = sorted(notrepeat(float(sanitize(each)) for each in c))
    i =i.replace('.txt','')
    #dic=i.append[c]
    print ('%s \'s fastest times are: ', %i, c2[0:3])
    
