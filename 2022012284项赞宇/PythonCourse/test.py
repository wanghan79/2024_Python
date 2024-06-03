from work3 import work3
from work2 import work2
from work1 import structDataSampling
import string
def txtFileToDataStrcut(filename):
    with open(filename, "r") as f:
        line = f.readlines()
    kw = {}
    data = {}
    for i in line:
        word = i.split()
        if len(word) == 1:
            num = int(word[0])
            kw["num"] = num
            continue
        type = word[0]
        if type == "int":
            data[type] = {"datarange": (int(word[1]), int(word[2]))}
        elif type == "float":
            data[type] = {"datarange": (float(word[1]), float(word[2]))}
        elif type == "str":
            data[type] = {"datarange": word[1], "strlen": int(word[2])}
        else:
            print("Occur Error")
            continue
        kw['struct']=data
        f.close()
    return kw

print('######################################test1##############################################')
kwargs = txtFileToDataStrcut("data.txt")
result = structDataSampling(**kwargs)
print('############################')
print("The dict in the file is: ", kwargs)
print("The generated data is:")
for item in result:
    print(item)
print('############################')

print('######################################test2##############################################')
kwargs = txtFileToDataStrcut("data.txt")
print('############################')
print("The dict in the file is: ", kwargs)
@work2("work2")
def test2(**dic):
    pass
test2(**kwargs)
print('############################')

print('######################################test3##############################################')
kwargs = txtFileToDataStrcut("data.txt")
@work3(**kwargs)
def test3(res):
    for item in res:
        print(item)
print('############################')
print("The dict in the file is: ", kwargs)
test3()
print('############################')