import json
from collections import OrderedDict

#切出x坐标
def extract_X(inputfile):
    file_obj = open(inputfile)
    all_line = file_obj.readlines()
    lineList = []
    for line in all_line:
        line = line.strip('\n')
        line = line.split(' ')
        length = len(line)
        line = line[:length:2]
        lineList.append(line)
    return lineList

#生成坐标
def generate_Y(n):
    lineList = []
    while n >= 320:
        lineList.append(n)
        n -= 10
    return lineList

#生成json文件
def generate_JsonFile(dic):
    jsonObj = json.dumps(dic)
    file = open('resultJson.json', 'w')
    file.write(jsonObj)
    file.close()

#聚合json字段
def gather_Json(lanes, h_samples, raw_file):
    d = OrderedDict()
    d[lanes] = lane
    d[h_samples] = h_sample
    d[raw_file] = "path/to/pic"
    return d


lane = []
h_sample = []
lane = extract_X('test.txt')
h_sample = generate_Y(580)

d = gather_Json("lanes", "h_samples", "raw_file")
generate_JsonFile(d)
