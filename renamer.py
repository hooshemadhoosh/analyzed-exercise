from os import listdir,rename
result = '\ufeff'
result += 'code,name\n'
print (listdir())
paths = [name for name in listdir() if name.endswith('.jpg')]
data = {key.split('_')[0]:[] for key in paths}
for path in paths:
    data[path.split('_')[0]]+=[path]

for i,dic in enumerate(data.items()):
    result+= f"{i+1},{dic[0]}\n"
    for path in dic[1]:
        newpath = path.replace(dic[0],str(i+1))
        print(path,newpath)
        rename(path,newpath)
with open('dictionary.csv','w',encoding='UTF-8') as f:
    f.write(result)
print(result)