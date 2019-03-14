import json

# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
file = open("papers.json", 'r', encoding='utf-8')
papers = []
for line in file.readlines():
    dic = json.loads(line)
    papers.append(dic)

print(papers[0:5])
print(len(papers))
